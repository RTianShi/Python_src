#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mutmut_log_and_type_pretty.py

在原脚本基础上美化输出格式。
保存后直接运行（不需要命令行参数）。修改 LOGFILE 路径以适配你的日志文件。
"""
from __future__ import annotations
import re
import sys
import textwrap
from typing import Dict, List, Tuple, Optional

# ------------------ 在这里替换日志路径 ------------------
LOGFILE = "/home/rts/下载/Python_src/logs/run_20251016_095948/chebyshevDist.log"
# --------------------------------------------------------

# try import libcst for AST-based detection
try:
    import libcst as cst
except Exception:
    cst = None

# --------------------- 基本解析函数（跟你原脚本相同/兼容） ---------------------
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
    m = re.match(r'^\s*MR(\d+)(?:_(\d+))?\s*$', mr, flags=re.IGNORECASE)
    if m:
        main = int(m.group(1))
        sub = int(m.group(2)) if m.group(2) else 0
        return (main, sub)
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
    for m in re.finditer(r'^\s*E\s+(\w+):\s+(.+)$', block_text, flags=re.MULTILINE):
        etype = m.group(1).strip()
        emsg = m.group(2).strip()
        info['runtime_errors'].append((etype, emsg))
    for m in re.finditer(r'(?m)^\s*(\w+Error|AssertionError|Exception):\s*(.+)$', block_text):
        etype = m.group(1).strip()
        emsg = m.group(2).strip()
        if not any(etype == e[0] and emsg == e[1] for e in info['runtime_errors']):
            info['runtime_errors'].append((etype, emsg))
    if re.search(r'FAIL|FAILED|FAILURE', block_text, flags=re.I):
        for m in re.finditer(r'(MR\d+(?:_\d+)?)', block_text, flags=re.IGNORECASE):
            info['mr_failures'].add(m.group(1).upper())
    return info

# ---------------------- 简单 defs 提取（全文件） ----------------------
def extract_all_defs_from_text(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    n = len(lines)
    defs: Dict[str, str] = {}
    i = 0
    header_re = re.compile(r'^(\s*)def\s+([A-Za-z0-9_]+)\s*\(.*\):\s*$')
    while i < n:
        m = header_re.match(lines[i])
        if m:
            header_indent = m.group(1)
            fname = m.group(2)
            block_lines = [lines[i]]
            i += 1
            while i < n:
                line = lines[i]
                if line.strip() == "":
                    block_lines.append(line); i += 1; continue
                indent_len = len(line) - len(line.lstrip())
                if indent_len > len(header_indent):
                    block_lines.append(line); i += 1; continue
                if indent_len == len(header_indent) and line.lstrip().startswith(("def ", "class ")):
                    break
                break
            src = "\n".join(block_lines).rstrip()
            if fname not in defs:
                defs[fname] = src
            continue
        i += 1
    return defs

# ---------------------- AST Collector & 检测（与之前实现一致） ----------------------
if cst:
    class Collector(cst.CSTVisitor):
        def __init__(self, module=None):
            self.module = module
            self.binary_ops = []
            self.comparisons = []
            self.calls = []
            self.literals = []
            self.assigns = []
            self.augassigns = []
            self.unarys = []
            self.lambdas = []
            self.matches = []
            self.subscripts = []
            self.names = []

        def visit_BinaryOperation(self, node): self.binary_ops.append(node)
        def visit_Comparison(self, node): self.comparisons.append(node)
        def visit_Call(self, node): self.calls.append(node)
        def visit_SimpleString(self, node): self.literals.append(node)
        def visit_Integer(self, node): self.literals.append(node)
        def visit_Float(self, node): self.literals.append(node)
        def visit_Imaginary(self, node): self.literals.append(node)
        def visit_Assign(self, node): self.assigns.append(node)
        def visit_AugAssign(self, node): self.augassigns.append(node)
        def visit_UnaryOperation(self, node): self.unarys.append(node)
        def visit_Lambda(self, node): self.lambdas.append(node)
        def visit_Match(self, node): self.matches.append(node)
        def visit_Subscript(self, node): self.subscripts.append(node)
        def visit_Name(self, node): self.names.append(node)
else:
    class Collector:
        def __init__(self, module=None):
            self.module = module
            self.binary_ops = []
            self.comparisons = []
            self.calls = []
            self.literals = []
            self.assigns = []
            self.augassigns = []
            self.unarys = []
            self.lambdas = []
            self.matches = []
            self.subscripts = []
            self.names = []

def code_for_node(mod, node):
    if not cst:
        return repr(node)
    try:
        return mod.code_for_node(node).strip()
    except Exception:
        return repr(node)

def choose_trace_evidence(trace: str) -> Optional[str]:
    if not trace:
        return None
    for line in trace.splitlines():
        if line.strip().startswith("E   ") or "Traceback" in line or "TypeError" in line or "unsupported operand" in line or "FAILED" in line:
            return line.strip()
    for line in trace.splitlines():
        if line.strip():
            return line.strip()
    return None

def detect_operators_from_pair(orig_src: str, mut_src: str, trace: str="") -> Tuple[List[str], str, List[str]]:
    ops: List[str] = []
    evidence_parts: List[str] = []
    if not cst:
        if "None" in mut_src and "None" not in orig_src:
            return (["operator_assignment"], "high", ["mutant contains None"])
        return (["_simple_mutation_mapping"], "low", ["no-libcst-fallback"])
    try:
        orig_mod = cst.parse_module(orig_src)
        mut_mod = cst.parse_module(mut_src)
    except Exception:
        if "NoneType" in trace:
            return (["operator_assignment"], "high", ["parse-fallback: trace contains 'NoneType'"])
        return (["_simple_mutation_mapping"], "low", ["parse-fallback: failed to parse functions"])

    orig_fn = next((n for n in orig_mod.body if isinstance(n, cst.FunctionDef)), orig_mod)
    mut_fn  = next((n for n in mut_mod.body if isinstance(n, cst.FunctionDef)), mut_mod)

    orig_col = Collector(orig_mod); mut_col = Collector(mut_mod)
    if isinstance(orig_fn, cst.CSTNode):
        orig_fn.visit(orig_col)
    if isinstance(mut_fn, cst.CSTNode):
        mut_fn.visit(mut_col)

    # assignment changes
    for o_a in getattr(orig_col, "assigns", []):
        try:
            o_t = [code_for_node(orig_mod, t.target) for t in o_a.targets]
            o_v = code_for_node(orig_mod, o_a.value) if o_a.value else ""
        except Exception:
            continue
        for m_a in getattr(mut_col, "assigns", []):
            try:
                m_t = [code_for_node(mut_mod, t.target) for t in m_a.targets]
                m_v = code_for_node(mut_mod, m_a.value) if m_a.value else ""
            except Exception:
                continue
            if o_t == m_t and o_v != m_v:
                ops.append("operator_assignment")
                evidence_parts.append(f"assign {o_t} {o_v} -> {m_v}")

    # augassign -> assign detection
    for aug in getattr(orig_col, "augassigns", []):
        try:
            tgt = code_for_node(orig_mod, aug.target)
        except Exception:
            tgt = None
        for m_a in getattr(mut_col, "assigns", []):
            try:
                mtgt = code_for_node(mut_mod, m_a.targets[0].target)
            except Exception:
                mtgt = None
            if m_a.targets and tgt and tgt == mtgt:
                ops.append("operator_augmented_assignment")
                evidence_parts.append(f"augassign {tgt} -> assign")

    # literals detection
    def collect_literals(col, mod):
        out = []
        for lit in getattr(col, "literals", []):
            try:
                out.append(code_for_node(mod, lit))
            except Exception:
                out.append(repr(lit))
        return out

    olits = collect_literals(orig_col, orig_mod)
    mlits = collect_literals(mut_col, mut_mod)

    for o in olits:
        for m in mlits:
            if o != m and re.search(r'\\d', o) and re.search(r'\\d', m):
                ops.append("operator_number"); evidence_parts.append(f"num {o}->{m}"); break
        if "operator_number" in ops:
            break

    for o in olits:
        for m in mlits:
            if o != m and (o.strip().startswith(("'", '"')) or m.strip().startswith(("'", '"'))):
                ops.append("operator_string"); evidence_parts.append(f"str {o}->{m}"); break
        if "operator_string" in ops:
            break

    # lambda
    for idx, ol in enumerate(getattr(orig_col, "lambdas", [])):
        if idx < len(getattr(mut_col, "lambdas", [])):
            try:
                o_b = code_for_node(orig_mod, ol.body)
                m_b = code_for_node(mut_mod, mut_col.lambdas[idx].body)
                if (o_b == "None" and m_b == "0") or (o_b == "0" and m_b == "None"):
                    ops.append("operator_lambda"); evidence_parts.append(f"lambda {o_b}->{m_b}")
            except Exception:
                continue

    # dict kw 'XX'
    for oc in getattr(orig_col, "calls", []):
        for mc in getattr(mut_col, "calls", []):
            try:
                fo = code_for_node(orig_mod, oc.func)
            except Exception:
                fo = ""
            if fo.endswith("dict") or fo == "dict":
                kws = [a.keyword.value if a.keyword else None for a in mc.args]
                if any(kw and "XX" in kw for kw in kws):
                    ops.append("operator_dict_arguments"); evidence_parts.append("dict kw contains 'XX'")

    # arg removal / arg->None
    for oc in getattr(orig_col, "calls", []):
        for mc in getattr(mut_col, "calls", []):
            try:
                fo = code_for_node(orig_mod, oc.func)
                fm = code_for_node(mut_mod, mc.func)
            except Exception:
                fo = fm = ""
            if fo == fm:
                if len(mc.args) < len(oc.args):
                    ops.append("operator_arg_removal"); evidence_parts.append(f"call {fo} args {len(oc.args)}->{len(mc.args)}")
                try:
                    o_vals = [code_for_node(orig_mod, a.value) for a in oc.args]
                    m_vals = [code_for_node(mut_mod, a.value) for a in mc.args]
                    for oa, ma in zip(o_vals, m_vals):
                        if oa != ma and ma.strip() == "None":
                            ops.append("operator_arg_removal"); evidence_parts.append(f"arg {oa}->None in {fo}")
                except Exception:
                    pass

    # string method swaps
    def attr_name(call_node, module):
        try:
            if isinstance(call_node.func, cst.Attribute):
                return code_for_node(module, call_node.func.attr)
        except Exception:
            pass
        return None

    for oc, mc in zip(getattr(orig_col, "calls", []), getattr(mut_col, "calls", [])):
        oa = attr_name(oc, orig_mod)
        ma = attr_name(mc, mut_mod)
        if oa and ma and oa != ma:
            sym = {("lower","upper"),("upper","lower"),("lstrip","rstrip"),("rstrip","lstrip"),
                   ("find","rfind"),("rfind","find"),("ljust","rjust"),("rjust","ljust"),
                   ("index","rindex"),("rindex","index"),("removeprefix","removesuffix"),("removesuffix","removeprefix"),
                   ("partition","rpartition"),("rpartition","partition")}
            if (oa, ma) in sym:
                ops.append("operator_symmetric_string_methods_swap"); evidence_parts.append(f"method {oa}->{ma}")
            elif (oa, ma) in {("split","rsplit"),("rsplit","split")}:
                ops.append("operator_unsymmetrical_string_methods_swap"); evidence_parts.append(f"split/rsplit {oa}->{ma}")

    # unary op removal
    for ou in getattr(orig_col, "unarys", []):
        try:
            if isinstance(ou.operator, (cst.Not, cst.BitInvert)):
                orepr = code_for_node(orig_mod, ou.expression)
                found = any(code_for_node(mut_mod, mu.expression) == orepr for mu in getattr(mut_col, "unarys", []))
                if not found:
                    ops.append("operator_remove_unary_ops"); evidence_parts.append(f"unary removed {orepr}")
        except Exception:
            continue

    # comparison keyword swap
    for oc in getattr(orig_col, "comparisons", []):
        for mc in getattr(mut_col, "comparisons", []):
            try:
                lo = code_for_node(orig_mod, oc.left)
                lm = code_for_node(mut_mod, mc.left)
            except Exception:
                lo = lm = None
            if lo == lm:
                o_ops = [type(c.operator) for c in oc.comparisons]
                m_ops = [type(c.operator) for c in mc.comparisons]
                if o_ops != m_ops:
                    kwpairs = {(cst.Is, cst.IsNot),(cst.IsNot,cst.Is),(cst.In,cst.NotIn),(cst.NotIn,cst.In)}
                    if any(pair in kwpairs for pair in set(zip(o_ops, m_ops))):
                        ops.append("operator_keywords"); evidence_parts.append("comp keyword swapped (is/in)")

    # name swaps
    for on in getattr(orig_col, "names", []):
        for mn in getattr(mut_col, "names", []):
            try:
                if on.value != mn.value:
                    if {on.value, mn.value} == {"True","False"}:
                        ops.append("operator_name"); evidence_parts.append("True<->False")
                    elif on.value == "deepcopy" and mn.value == "copy":
                        ops.append("operator_name"); evidence_parts.append("deepcopy->copy")
            except Exception:
                pass

    # binary op swap
    for ob, mb in zip(getattr(orig_col, "binary_ops", []), getattr(mut_col, "binary_ops", [])):
        try:
            oleft = code_for_node(orig_mod, ob.left)
            oright = code_for_node(orig_mod, ob.right)
            mleft = code_for_node(mut_mod, mb.left)
            mright = code_for_node(mut_mod, mb.right)
        except Exception:
            continue
        if oleft == mleft and oright == mright and type(ob.operator) != type(mb.operator):
            ops.append("operator_swap_op"); evidence_parts.append(f"{type(ob.operator).__name__}->{type(mb.operator).__name__}")

    # match-case removal
    for om in getattr(orig_col, "matches", []):
        for mm in getattr(mut_col, "matches", []):
            if len(mm.cases) < len(om.cases):
                ops.append("operator_match"); evidence_parts.append(f"match cases {len(om.cases)}->{len(mm.cases)}")

    # subscript/slice change
    for osub, msub in zip(getattr(orig_col, "subscripts", []), getattr(mut_col, "subscripts", [])):
        if code_for_node(orig_mod, osub) != code_for_node(mut_mod, msub):
            ops.append("operator_swap_op"); evidence_parts.append("subscript/slice changed")

    if "NoneType" in trace and "operator_assignment" not in ops:
        ops.insert(0, "operator_assignment")
        evidence_parts.insert(0, "trace indicates NoneType")

    ops = list(dict.fromkeys(ops))
    evidence_parts = list(dict.fromkeys(evidence_parts))

    if ("operator_assignment" in ops and "NoneType" in trace) or any(ep.startswith("assign") for ep in evidence_parts):
        confidence = "high"
    elif len(ops) <= 2:
        confidence = "medium"
    else:
        confidence = "low"

    return ops, confidence, evidence_parts

# ---------------------- 辅助：从 block 中提取 mutant 源代码并寻找原函数 ----------------------
def find_mutant_src(mut_name: str, block_raw: str, defs_map: Dict[str, str]) -> str:
    if mut_name in defs_map:
        return defs_map[mut_name]
    m = re.search(r'函数源码如下[:：]?\s*$', block_raw, flags=re.M)
    if m:
        after = block_raw[m.end():]
        mm = re.search(r'^\s*def\s+' + re.escape(mut_name) + r'\s*\(.*\):.*$', after, flags=re.M)
        if mm:
            lines_local = after.splitlines()
            for i, ln in enumerate(lines_local):
                if re.match(r'^\s*def\s+' + re.escape(mut_name) + r'\s*\(.*\):.*$', ln):
                    header_indent = re.match(r'^(\s*)', ln).group(1)
                    block = [ln]
                    j = i+1
                    while j < len(lines_local):
                        l2 = lines_local[j]
                        if l2.strip() == "":
                            block.append(l2); j += 1; continue
                        indent_len = len(l2) - len(l2.lstrip())
                        if indent_len > len(header_indent):
                            block.append(l2); j += 1; continue
                        break
                    return "\n".join(block).rstrip()
    mm = re.search(r'^\s*def\s+' + re.escape(mut_name) + r'\s*\(.*\):.*$', block_raw, flags=re.M)
    if mm:
        start = mm.start()
        snippet = block_raw[start: start + 2000]
        return "\n".join(snippet.splitlines()[:10]).rstrip()
    return ""

def find_orig_src_for(mut_name: str, defs_map: Dict[str, str]) -> Optional[str]:
    mo = re.match(r"(?P<base>.+)__mutmut_\d+$", mut_name)
    if mo:
        candidate = mo.group("base") + "__mutmut_orig"
        if candidate in defs_map:
            return defs_map[candidate]
        for k, v in defs_map.items():
            if k == candidate:
                return v
        for k, v in defs_map.items():
            if k.endswith("__mutmut_orig") and mo.group("base") in k:
                return v
    for k, v in defs_map.items():
        if k.endswith("__mutmut_orig"):
            return v
    return None

# ---------------------- 美化输出函数 ----------------------
def pretty_print_report(parsed: List[Dict], defs_map: Dict[str, str]):
    original_infos = [p for p in parsed if re.search(r'orig', p['mutant'], re.I) or re.search(r'_orig$', p['mutant'], re.I)]
    original_passed = None
    original_name = None
    if original_infos:
        orig = original_infos[0]
        original_passed = orig['passed_bool']
        original_name = orig['mutant']

    killed, runtime_err, survived, other = [], [], [], []
    for p in parsed:
        name = p['mutant']
        if original_name and name == original_name: continue
        has_runtime = len(p['runtime_errors']) > 0
        has_mr = len(p['mr_failures']) > 0
        failed = (p['failed'] > 0) or has_runtime or has_mr
        if original_passed is True and failed:
            if has_runtime: runtime_err.append(name)
            else: killed.append(name)
        else:
            if p['passed_bool'] and not failed: survived.append(name)
            else:
                if has_runtime: runtime_err.append(name)
                else: other.append(name)

    # Summary
    if original_name:
        print("原函数通过" if original_passed else "原函数未通过")
    else:
        print("原函数未找到（日志中没有明显标识含 'orig' 的条目）")
    print()
    print("被杀死突变体：", ", ".join(killed) if killed else "无")
    print("运行报错突变体：", ", ".join(sorted(set(runtime_err))) if runtime_err else "无")
    print("幸存突变体：", ", ".join(survived) if survived else "无")
    print("-" * 37)

    # Build detailed rows
    rows = []
    for p in parsed:
        name = p['mutant']
        if original_name and name == original_name: continue
        status = "ERROR" if p['runtime_errors'] else ("FAIL" if p['failed']>0 or p['mr_failures'] else ("PASS" if p['passed_bool'] else "UNKNOWN"))
        mr_list = sorted(list(p['mr_failures']), key=mr_key)
        mr_txt = "，".join(mr_list) if mr_list else ""
        # detect operators
        mut_src = find_mutant_src(name, p['raw'], defs_map)
        orig_src = find_orig_src_for(name, defs_map)
        if orig_src and mut_src and cst:
            ops, conf, evidence_parts = detect_operators_from_pair(orig_src, mut_src, p['raw'])
            ops_txt = ";".join(ops) if ops else "_simple_mutation_mapping"
            evidence = "; ".join(evidence_parts) if evidence_parts else choose_trace_evidence(p['raw']) or (mut_src.strip().splitlines()[0] if mut_src.strip() else "no-evidence")
        else:
            ops_txt = "_simple_mutation_mapping"
            conf = "low"
            evidence = choose_trace_evidence(p['raw']) or (mut_src.strip().splitlines()[0] if mut_src.strip() else "original not found in same log file")
        # If runtime_errors present, show first
        if p['runtime_errors']:
            evidence = f"‼ {p['runtime_errors'][0][0]}: {p['runtime_errors'][0][1]}"
        rows.append({
            "mutant": name,
            "status": status,
            "mr": mr_txt,
            "operators": ops_txt,
            "confidence": conf,
            "evidence": evidence
        })

    # Compute column widths and pretty-print table
    col_names = ["Mutant", "Status", "MR(s)", "Operators", "Confidence", "Evidence"]
    # Determine widths (max but clamp evidence)
    col_widths = {k: len(k) for k in col_names}
    for r in rows:
        col_widths["Mutant"] = max(col_widths["Mutant"], len(r["mutant"]))
        col_widths["Status"] = max(col_widths["Status"], len(r["status"]))
        col_widths["MR(s)"] = max(col_widths["MR(s)"], len(r["mr"]))
        col_widths["Operators"] = max(col_widths["Operators"], len(r["operators"]))
        col_widths["Confidence"] = max(col_widths["Confidence"], len(r["confidence"]))
    # cap evidence column width for wrapping
    max_total_width = 110
    left_cols_width = (col_widths["Mutant"] + col_widths["Status"] + col_widths["MR(s)"] +
                       col_widths["Operators"] + col_widths["Confidence"] + 5*3)  # 3 spaces between cols
    evidence_width = max(20, min(60, max_total_width - left_cols_width))
    col_widths["Evidence"] = evidence_width

    # Header
    header = f"{'Mutant'.ljust(col_widths['Mutant'])}   {'Status'.ljust(col_widths['Status'])}   {'MR(s)'.ljust(col_widths['MR(s)'])}   {'Operators'.ljust(col_widths['Operators'])}   {'Confidence'.ljust(col_widths['Confidence'])}   Evidence"
    print(header)
    print("-" * len(header))

    # Rows with wrapping evidence
    for r in rows:
        ev_lines = textwrap.wrap(r["evidence"], width=col_widths["Evidence"]) or [""]
        first = f"{r['mutant'].ljust(col_widths['Mutant'])}   {r['status'].ljust(col_widths['Status'])}   {r['mr'].ljust(col_widths['MR(s)'])}   {r['operators'].ljust(col_widths['Operators'])}   {r['confidence'].ljust(col_widths['Confidence'])}   {ev_lines[0]}"
        print(first)
        for cont in ev_lines[1:]:
            print(" " * (col_widths['Mutant'] + 3 + col_widths['Status'] + 3 + col_widths['MR(s)'] + 3 + col_widths['Operators'] + 3 + col_widths['Confidence'] + 3) + cont)
    print()

    # ------------------ 额外统计：总数、被杀死、幸存、运行报错、UNKNOWN ------------------
    # 统计时排除原函数（如果存在）
    total = sum(1 for p in parsed if not (original_name and p['mutant'] == original_name))
    killed_count = len(killed)
    runtime_err_count = len(set(runtime_err))
    survived_count = len(survived)
    other_count = len(other)
    unknown_count = sum(1 for r in rows if r['status'] == 'UNKNOWN' or r['mutant'] == 'UNKNOWN')

    print("统计：")
    print(f"  总数 (不含原函数): {total}")
    print(f"  被杀死数量: {killed_count}")
    print(f"  运行报错数量: {runtime_err_count}")
    print(f"  幸存数量: {survived_count}")
    print(f"  其他/未确定数量: {other_count}")
    print(f"  UNKNOWN 数量: {unknown_count}")
    print("-" * 37)

# ---------------------- main ----------------------
def main():
    try:
        with open(LOGFILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"无法读取日志文件 '{LOGFILE}': {e}", file=sys.stderr)
        sys.exit(2)

    defs_map = extract_all_defs_from_text(text)
    blocks = split_blocks(text)
    parsed = []
    for mutant, file_part, block_text in blocks:
        info = parse_block(mutant, file_part, block_text)
        parsed.append(info)

    pretty_print_report(parsed, defs_map)

if __name__ == '__main__':
    main()