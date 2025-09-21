# conftest.py
import os, json, re
from pathlib import Path
import pytest

LOG_DIR = Path("pytest_mutant_logs")
LOG_DIR.mkdir(exist_ok=True)

def _first_nonempty(lines):
    for l in lines:
        if l and l.strip():
            return l.strip()
    return None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # 只关注测试执行阶段的失败
    if rep.when == "call" and rep.failed:
        mutant_id = os.environ.get("MUTANT_ID", "unknown")
        nodeid = item.nodeid
        longrepr_text = getattr(rep, "longreprtext", None) or str(getattr(rep, "longrepr", ""))

        # 默认字段
        file = None
        line = None
        assert_expr = None
        failure_reason = None
        exc_type = None
        exc_msg = None

        # 1) 若 longrepr 是 pytest 对象，尝试用其属性抽取
        lr_obj = getattr(rep, "longrepr", None)
        try:
            reprcrash = getattr(lr_obj, "reprcrash", None)
            if reprcrash:
                p = getattr(reprcrash, "path", None)
                ln = getattr(reprcrash, "lineno", None)
                if p:
                    file = str(p)
                if ln:
                    try:
                        line = int(ln)
                    except Exception:
                        pass
                msg = getattr(reprcrash, "message", None)
                if msg:
                    exc_msg = str(msg)
                    m = re.match(r'([A-Za-z_0-9]+)(?:\:)?\s*(.*)', exc_msg)
                    if m:
                        exc_type = m.group(1)
        except Exception:
            pass

        # 2) 回退到文本解析：File "path", line N
        if not file or not line:
            m = re.search(r'File \"([^\"]+)\", line (\d+)', longrepr_text)
            if m:
                file = file or m.group(1)
                try:
                    line = line or int(m.group(2))
                except Exception:
                    pass

        # 3) 回退到简短格式： path:lineno: ...
        if not file or not line:
            m2 = re.search(r'([^\s:][^:\n]+):(\d+)(?:[:\s]|$)', longrepr_text)
            if m2:
                file = file or m2.group(1)
                try:
                    line = line or int(m2.group(2))
                except Exception:
                    pass

        # 4) 识别 check / 自定义输出 (例如 "FAILURE: check 15 == 0: MR2 failed")
        m_check = re.search(r'FAILURE:\s*(check\s+(.+?)\s*:\s*(MR[0-9A-Za-z_\-]+|.+))', longrepr_text, re.IGNORECASE)
        if m_check:
            maybe_expr = m_check.group(2).strip()
            assert_expr = maybe_expr
            if re.search(r'MR[0-9A-Za-z_\-]+', longrepr_text, re.IGNORECASE):
                mr = re.search(r'(MR[0-9A-Za-z_\-]+(?:_\d+)?)\s*failed', longrepr_text, re.IGNORECASE)
                if mr:
                    failure_reason = mr.group(0)
            exc_type = exc_type or "check"
            exc_msg = exc_msg or maybe_expr

        # 5) 若没 extract 出断言，尝试寻找 assert 行或 "E       assert ..." 或 "assert "
        if not assert_expr:
            for l in longrepr_text.splitlines():
                ls = l.strip()
                if ls.startswith("E       assert") or ls.startswith("assert "):
                    assert_expr = re.sub(r'^E\s*', '', ls)
                    break

        # 6) 若还没 exc_type, 尝试从最后几行解析异常类型
        if not exc_type:
            last_nonempty = _first_nonempty(longrepr_text.splitlines()[-5:])
            if last_nonempty:
                m3 = re.search(r'([A-Za-z_0-9]+Error|Exception|AssertionError|Failure|FAILURE)(?:\:)?\s*(.*)', last_nonempty)
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
            "failure_reason": failure_reason,
            "exc_type": exc_type,
            "exc_msg": exc_msg,
            "longrepr": longrepr_text.replace("\n","\\n")
        }

        safe_node = nodeid.replace("/", "__").replace("::", "__").replace(":", "_")
        out_path = LOG_DIR / f"{mutant_id}__{safe_node}.json"
        try:
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=2)
        except Exception:
            pass
