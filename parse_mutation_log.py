#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_mutation_log.py（无需命令行参数）
内置日志路径 LOGFILE，输出简洁报告并按数值排序 MR 列表（支持 MRn 和 MRn_m）。
"""
import re
import sys
import json

# ------------------ 在这里替换日志路径 & 输出选项 ------------------
LOGFILE = "/home/rts/下载/Python_src/logs/run_20250924_202833/add_values.log"          # <-- 把这里改成你的日志文件路径
OUTPUT_JSON = False          # <-- 是否同时生成 JSON 输出文件
OUTPUT_JSON_PATH = "report.json"
# ------------------------------------------------------------------

def split_blocks(text):
    pattern = re.compile(r'RUNNING\s+(.+?)\s+::\s+(.+?)\s+-\s+(\S+)', re.MULTILINE)
    matches = list(pattern.finditer(text))
    blocks = []
    if not matches:
        blocks.append(("UNKNOWN", None, text))
        return blocks

    for i, m in enumerate(matches):
        file_part = m.group(1).strip()
        mutant = m.group(2).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        block_text = text[start:end]
        blocks.append((mutant, file_part, block_text))
    return blocks

def mr_key(mr):
    """
    把 MR 字符串解析成排序键 (main_int, sub_int)
    支持:
      MR5 -> (5, 0)
      MR12 -> (12, 0)
      MR3_1 -> (3, 1)
      MR3_2 -> (3, 2)
    若无法解析，放到后面（用大数值键）。
    """
    m = re.match(r'^\s*MR(\d+)(?:_(\d+))?\s*$', mr, flags=re.IGNORECASE)
    if m:
        main = int(m.group(1))
        sub = int(m.group(2)) if m.group(2) else 0
        return (main, sub)
    # 非标准格式放到后面
    return (10**9, 0)

def parse_block(mutant, file_part, block_text):
    info = {
        'mutant': mutant,
        'file': file_part,
        'passed': 0,
        'failed': 0,
        'duration': None,
        'exit_code': None,
        'mr_failures': set(),
        'runtime_errors': [],
        'passed_bool': False,
        'raw': block_text
    }

    m_pass = re.search(r'(\d+)\s+passed\s+in\s+([\d.]+)s', block_text)
    m_fail = re.search(r'(\d+)\s+failed\s+in\s+([\d.]+)s', block_text)
    if m_pass:
        info['passed'] = int(m_pass.group(1))
        try:
            info['duration'] = float(m_pass.group(2))
        except:
            pass
    if m_fail:
        info['failed'] = int(m_fail.group(1))
        try:
            info['duration'] = float(m_fail.group(2))
        except:
            pass

    m_x = re.search(r'❌\s+.+?存在失败(?:\s*\(退出码\s*(\d+)\))?', block_text)
    if m_x and m_x.group(1):
        try:
            info['exit_code'] = int(m_x.group(1))
        except:
            pass

    if re.search(r'✅\s+.+?所有测试通过', block_text) or (info['failed'] == 0 and info['passed'] > 0):
        info['passed_bool'] = True

    # runtime errors: "E   TypeError: ..." style
    for m in re.finditer(r'^\s*E\s+(\w+):\s+(.+)$', block_text, flags=re.MULTILINE):
        etype = m.group(1).strip()
        emsg = m.group(2).strip()
        info['runtime_errors'].append((etype, emsg))

    # looser fallback capture
    for m in re.finditer(r'(?m)^\s*(\w+Error|AssertionError|Exception):\s*(.+)$', block_text):
        etype = m.group(1).strip()
        emsg = m.group(2).strip()
        if not any(etype == e[0] and emsg == e[1] for e in info['runtime_errors']):
            info['runtime_errors'].append((etype, emsg))

    # 收集 MR：只在包含失败信息的块内收集 MR
    if re.search(r'FAIL|FAILED|FAILURE', block_text, flags=re.I):
        for m in re.finditer(r'(MR\d+(?:_\d+)?)', block_text, flags=re.IGNORECASE):
            info['mr_failures'].add(m.group(1).upper())

    return info

def generate_report(parsed):
    # find original
    original_infos = [p for p in parsed if re.search(r'orig', p['mutant'], re.I) or re.search(r'_orig$', p['mutant'], re.I)]
    original_passed = None
    original_name = None
    if original_infos:
        orig = original_infos[0]
        original_passed = orig['passed_bool']
        original_name = orig['mutant']

    killed = []
    runtime_err = []
    survived = []
    other = []

    for p in parsed:
        name = p['mutant']
        if original_name and name == original_name:
            continue
        has_runtime = len(p['runtime_errors']) > 0
        has_mr = len(p['mr_failures']) > 0
        failed = (p['failed'] > 0) or has_runtime or has_mr
        if original_passed is True and failed:
            if has_runtime:
                runtime_err.append(name)
            else:
                killed.append(name)
        else:
            if p['passed_bool'] and not failed:
                survived.append(name)
            else:
                if has_runtime:
                    runtime_err.append(name)
                else:
                    other.append(name)

    lines = []
    if original_name:
        header = "原函数通过" if original_passed else "原函数未通过"
    else:
        header = "原函数未找到（日志中没有明显标识含 'orig' 的条目）"
    lines.append(header)
    lines.append("")
    lines.append("被杀死突变体：" + (", ".join(killed) if killed else "无"))
    lines.append("运行报错突变体：" + (", ".join(sorted(set(runtime_err))) if runtime_err else "无"))
    lines.append("幸存突变体：" + (", ".join(survived) if survived else "无"))
    lines.append("-------------------------------------")

    # 详细部分：按数值顺序显示 MR 列表
    for p in parsed:
        name = p['mutant']
        if original_name and name == original_name:
            continue
        mr_list = list(p['mr_failures'])
        if p['runtime_errors']:
            rmsgs = []
            seen = set()
            for et, em in p['runtime_errors']:
                key = f"{et}: {em}"
                if key not in seen:
                    seen.add(key)
                    rmsgs.append(key)
            lines.append(f"{name}：（运行报错）" + "；".join(rmsgs))
        elif mr_list:
            # 按数值化键排序后再输出
            mr_sorted = sorted(mr_list, key=mr_key)
            lines.append(f"{name}：" + "，".join(mr_sorted))
        else:
            if p['passed_bool']:
                lines.append(f"{name}：幸存（通过）")
            else:
                lines.append(f"{name}：未通过，但未检测到 MR 或 运行时错误（需要人工检查）")

    text_report = "\n".join(lines)
    return text_report, {
        'original': {'name': original_name, 'passed': original_passed},
        'killed': killed,
        'runtime_error': sorted(set(runtime_err)),
        'survived': survived,
        'other': other,
        'details': parsed
    }

def main():
    try:
        with open(LOGFILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"无法读取日志文件 '{LOGFILE}': {e}", file=sys.stderr)
        sys.exit(2)

    blocks = split_blocks(text)
    parsed = []
    for mutant, file_part, block_text in blocks:
        info = parse_block(mutant, file_part, block_text)
        parsed.append(info)

    text_report, json_obj = generate_report(parsed)
    print(text_report)

    if OUTPUT_JSON:
        try:
            with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as jf:
                json.dump(json_obj, jf, ensure_ascii=False, indent=2)
            print(f"\nJSON 报告已写入: {OUTPUT_JSON_PATH}")
        except Exception as e:
            print("写入 JSON 文件失败：", e, file=sys.stderr)

if __name__ == '__main__':
    main()
