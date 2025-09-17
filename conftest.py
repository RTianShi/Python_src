# conftest.py （改进版）
import os
import json
import re
from pathlib import Path
import pytest

LOG_DIR = Path("pytest_mutant_logs")
LOG_DIR.mkdir(exist_ok=True)

def _extract_from_longrepr_obj(lr_obj):
    """
    从 pytest 的 longrepr 对象尝试提取 path, lineno, exc_type, exc_msg。
    返回 (path_or_None, lineno_or_None, exc_type_or_None, exc_msg_or_None)
    """
    try:
        # many pytest versions expose reprcrash with path & lineno
        reprcrash = getattr(lr_obj, "reprcrash", None)
        if reprcrash is not None:
            path = getattr(reprcrash, "path", None)
            lineno = getattr(reprcrash, "lineno", None)
            # reprcrash.message 常包含 "ZeroDivisionError: ..." 或 "message"
            msg = getattr(reprcrash, "message", None)
            # infer exception type from message if possible
            exc_type = None
            if msg and isinstance(msg, str):
                m = re.match(r'([A-Za-z_0-9]+)(?:\:)?', msg)
                if m:
                    exc_type = m.group(1)
            return path, lineno, exc_type, msg
    except Exception:
        pass
    # try reprtraceback entries as fallback
    try:
        rtb = getattr(lr_obj, "reprtraceback", None)
        if rtb is not None:
            entries = getattr(rtb, "reprentries", []) or []
            # pick the last entry that has a lineno/path
            for e in reversed(entries):
                # reprentry may have reprfileloc with path/lineno
                rf = getattr(e, "reprfileloc", None)
                if rf:
                    path = getattr(rf, "path", None)
                    lineno = getattr(rf, "lineno", None)
                    return path, lineno, None, None
    except Exception:
        pass
    return None, None, None, None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mutant_id = os.environ.get("MUTANT_ID", "unknown")
        nodeid = item.nodeid
        # 获取 longrepr 兼容不同类型：字符串或对象
        longrepr_text = getattr(rep, "longreprtext", None) or str(getattr(rep, "longrepr", ""))
        # 初始化
        file = None
        line = None
        assert_expr = None
        exc_type = None
        exc_msg = None

        # 1) 优先从 longrepr 的对象结构中抽取（更稳）
        lr_obj = getattr(rep, "longrepr", None)
        if lr_obj is not None:
            try:
                f, ln, et, em = _extract_from_longrepr_obj(lr_obj)
                if f:
                    file = f
                if ln:
                    line = int(ln)
                if et:
                    exc_type = et
                if em:
                    exc_msg = em
            except Exception:
                pass

        # 2) 回退：标准 traceback 格式 File "path", line N
        if not file or not line:
            m = re.search(r'File \"([^\"]+)\", line (\d+)', longrepr_text)
            if m:
                file = file or m.group(1)
                line = line or int(m.group(2))

        # 3) 回退：简短格式 path:lineno: ExceptionName
        if not file or not line:
            # 匹配 like "../src/add_values.py:4: ZeroDivisionError"
            m2 = re.search(r'([^\s:][^:\n]+):(\d+):\s*([A-Za-z_0-9]+)(?:\:?\s*(.*))?', longrepr_text)
            if m2:
                file = file or m2.group(1)
                line = line or int(m2.group(2))
                if not exc_type and m2.group(3):
                    exc_type = m2.group(3)
                if not exc_msg and m2.group(4):
                    exc_msg = (m2.group(4) or "").strip()

        # 4) 提取断言表达式（若有）
        # pytest longrepr 中断言行常以 "E       assert ..." 或直接 "assert ..." 出现
        for l in longrepr_text.splitlines():
            ls = l.strip()
            if ls.startswith("E       assert") or ls.startswith("assert "):
                # 规范化，去掉前缀的 "E       "
                assert_expr = re.sub(r'^E\s*', '', ls)
                break

        # 5) 如果 exc_type 仍然空，可尝试从最末尾的异常行解析
        if not exc_type:
            # 找类似 "ZeroDivisionError: integer division or modulo by zero"
            m3 = re.search(r'([A-Za-z_0-9]+Error|Exception)(?:\:)?\s*(.*)', longrepr_text.splitlines()[-1])
            if m3:
                exc_type = m3.group(1)
                if not exc_msg:
                    exc_msg = m3.group(2).strip() if m3.group(2) else None

        record = {
            "mutant_id": mutant_id,
            "nodeid": nodeid,
            "file": file,
            "line": line,
            "assert_expr": assert_expr,
            "exc_type": exc_type,
            "exc_msg": exc_msg,
            "longrepr": longrepr_text.replace("\n", "\\n")
        }

        safe_node = nodeid.replace("/", "__").replace("::", "__").replace(":", "_")
        out_path = LOG_DIR / f"{mutant_id}__{safe_node}.json"
        try:
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=2)
        except Exception:
            pass
