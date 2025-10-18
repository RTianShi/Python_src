#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mutmut_log_classifier_v6.py

更鲁棒地解析 mutmut 日志（放宽 header 正则、增大搜索窗口）。
将结果写入 CSV（默认 OUT_CSV）。

依赖: libcst
  pip install libcst
"""
from __future__ import annotations
import re
import csv
import sys
from typing import Dict, List, Tuple, Optional

try:
    import libcst as cst
except Exception:
    print("Error: this script requires libcst. Install with: pip install libcst", file=sys.stderr)
    raise

# ---------------------- 配置（修改为你的路径） ----------------------
INPUT_PATH = '/home/rts/下载/Python_src/logs/run_20251007_104605/add_values.log'
OUT_CSV = 'mutmut_classification_results_v6.csv'
DEBUG = False  # 如需调试，设为 True（会在 stderr 打印解析到的 mutant 列表与状态）
# --------------------------------------------------------------------

# ---------------- Relaxed regexes ----------------
# 支持前导空白、中文或 ascii 冒号、不强求行尾完全匹配
DEF_HEADER_RE = re.compile(r'^(\s*)def\s+([A-Za-z0-9_]+)\s*\(.*\):\s*$', re.M)
MUTANT_MARKER_CHINESE_RE = re.compile(
    r'^\s*>{3}\s*当前使用的函数\s*[:：]\s*(?P<mutant>[A-Za-z0-9_]+)\b', re.M)
MUTANT_MARKER_RUNNING_RE = re.compile(
    r'^\s*=+\s*RUNNING\b.*::\s*(?P<mutant>[A-Za-z0-9_]+)\b', re.M)
RUNNING_RE = re.compile(r'^\s*=+\s*RUNNING\b', re.M)
SEPARATOR_LINE_RE = re.compile(r'^\s*={3,}\s*$')

# ---------------- extract all defs ----------------
def extract_all_defs(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    n = len(lines)
    defs: Dict[str, str] = {}
    i = 0
    while i < n:
        m = DEF_HEADER_RE.match(lines[i])
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
                header_indent_len = len(header_indent)
                if indent_len > header_indent_len:
                    block_lines.append(line); i += 1; continue
                if indent_len == header_indent_len and line.lstrip().startswith(("def ", "class ")):
                    break
                break
            src = "\n".join(block_lines).rstrip()
            if fname not in defs:
                defs[fname] = src
            continue
        i += 1
    return defs

# ---------------- robust parse_log_file (v6) ----------------
def parse_log_file(path: str) -> Tuple[Dict[str, Dict], Dict[str, str]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        raise RuntimeError(f"Unable to read log file {path}: {e}")

    defs = extract_all_defs(text)
    lines = text.splitlines()
    n = len(lines)
    mutants: Dict[str, Dict] = {}

    def find_def_forward(start: int, target_name: Optional[str] = None, max_scan: int = 5000) -> Tuple[Optional[int], str]:
        end = min(n, start + max_scan)
        i = start
        while i < end:
            m = DEF_HEADER_RE.match(lines[i])
            if m:
                name = m.group(2)
                if (target_name is None) or (name == target_name):
                    header_indent = m.group(1)
                    block_lines = [lines[i]]
                    i2 = i + 1
                    while i2 < n:
                        line = lines[i2]
                        if line.strip() == "":
                            block_lines.append(line); i2 += 1; continue
                        indent_len = len(line) - len(line.lstrip())
                        header_indent_len = len(header_indent)
                        if indent_len > header_indent_len:
                            block_lines.append(line); i2 += 1; continue
                        if indent_len == header_indent_len and line.lstrip().startswith(("def ", "class ")):
                            break
                        break
                    return i, "\n".join(block_lines).rstrip()
            i += 1
        return None, ""

    i = 0
    while i < n:
        line = lines[i]
        m_ch = MUTANT_MARKER_CHINESE_RE.match(line)
        m_run = None
        if not m_ch:
            m_run = MUTANT_MARKER_RUNNING_RE.match(line)
        m = m_ch or m_run
        if m:
            mname = m.group("mutant")
            found_src = ""
            found_idx = None

            # 增大搜索范围：优先搜索 '函数源码如下' 标记（在 header 后 2000 行内）
            marker_search_end = min(n, i + 2000)
            src_marker_idx = None
            k = i + 1
            while k < marker_search_end:
                if lines[k].strip().startswith("函数源码如下"):
                    src_marker_idx = k
                    break
                k += 1
            if src_marker_idx is not None:
                p = src_marker_idx + 1
                while p < n and lines[p].strip() == "":
                    p += 1
                def_idx, def_src = find_def_forward(p, target_name=mname, max_scan=5000)
                if def_idx is None:
                    if p < n:
                        mm = DEF_HEADER_RE.match(lines[p])
                        if mm:
                            def_idx, def_src = find_def_forward(p, target_name=None, max_scan=5000)
                if def_src:
                    found_src = def_src
                    found_idx = def_idx

            if not found_src:
                def_idx, def_src = find_def_forward(i+1, target_name=mname, max_scan=5000)
                if def_src:
                    found_src = def_src
                    found_idx = def_idx
                else:
                    found_src = defs.get(mname, "")

            trace_lines = []
            j = i + 1
            while j < n:
                if RUNNING_RE.match(lines[j]) or SEPARATOR_LINE_RE.match(lines[j]):
                    break
                trace_lines.append(lines[j])
                j += 1
            trace_text = "\n".join(trace_lines).strip()
            status = "PASS"
            if "FAIL" in trace_text or "FAILED" in trace_text or re.search(r"^\s*E\s+", trace_text, re.M) or trace_text.count("failed")>0:
                status = "FAIL"

            if mname in mutants:
                prev = mutants[mname]
                prev_trace = prev.get("trace", "")
                combined_trace = prev_trace + ("\n" + trace_text if trace_text else "")
                prev["trace"] = combined_trace
                if not prev.get("mut_src") and found_src:
                    prev["mut_src"] = found_src
            else:
                mutants[mname] = {"mut_src": found_src, "trace": trace_text, "status": status}

            i = j
            continue
        i += 1

    if DEBUG:
        print("DEBUG: parsed mutant names:", file=sys.stderr)
        for name, info in mutants.items():
            print(f"  - {name}  (has_src={bool(info.get('mut_src'))}, status={info.get('status')})", file=sys.stderr)
        print("DEBUG: defs keys sample:", file=sys.stderr)
        cnt = 0
        for k in defs.keys():
            print("  def", k, file=sys.stderr)
            cnt += 1
            if cnt >= 30: break

    return mutants, defs

# ---------------- AST collector & helper (same as prior) ----------------
class Collector(cst.CSTVisitor):
    def __init__(self, module: cst.Module):
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

def code_for_node(mod: cst.Module, node: cst.CSTNode) -> str:
    try:
        return mod.code_for_node(node).strip()
    except Exception:
        return repr(node)

# ---------------- detection (same as v5) ----------------
def detect_operators_from_pair(orig_src: str, mut_src: str, trace: str="") -> Tuple[List[str], str, List[str]]:
    # (implementation identical to previous script)
    ops: List[str] = []
    evidence_parts: List[str] = []

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
    orig_fn.visit(orig_col); mut_fn.visit(mut_col)

    # assignment changes
    for o_a in orig_col.assigns:
        try:
            o_t = [code_for_node(orig_mod, t.target) for t in o_a.targets]
            o_v = code_for_node(orig_mod, o_a.value) if o_a.value else ""
        except Exception:
            continue
        for m_a in mut_col.assigns:
            try:
                m_t = [code_for_node(mut_mod, t.target) for t in m_a.targets]
                m_v = code_for_node(mut_mod, m_a.value) if m_a.value else ""
            except Exception:
                continue
            if o_t == m_t and o_v != m_v:
                ops.append("operator_assignment")
                evidence_parts.append(f"assign {o_t} {o_v} -> {m_v}")

    # augassign -> assign
    if orig_col.augassigns:
        for aug in orig_col.augassigns:
            try:
                tgt = code_for_node(orig_mod, aug.target)
            except Exception:
                tgt = None
            for m_a in mut_col.assigns:
                if m_a.targets and tgt and tgt == code_for_node(mut_mod, m_a.targets[0].target):
                    ops.append("operator_augmented_assignment")
                    evidence_parts.append(f"augassign {tgt} -> assign")

    # literals detection
    def collect_literals(col, mod):
        out = []
        for lit in col.literals:
            try:
                out.append(code_for_node(mod, lit))
            except Exception:
                out.append(repr(lit))
        return out

    olits = collect_literals(orig_col, orig_mod)
    mlits = collect_literals(mut_col, mut_mod)

    for o in olits:
        for m in mlits:
            if o != m and re.search(r'\d', o) and re.search(r'\d', m):
                ops.append("operator_number"); evidence_parts.append(f"num {o}->{m}"); break
        if "operator_number" in ops:
            break

    for o in olits:
        for m in mlits:
            if o != m and (o.strip().startswith(("'", '"')) or m.strip().startswith(("'", '"'))):
                ops.append("operator_string"); evidence_parts.append(f"str {o}->{m}"); break
        if "operator_string" in ops:
            break

    # lambda None <-> 0
    for idx, ol in enumerate(orig_col.lambdas):
        if idx < len(mut_col.lambdas):
            try:
                o_b = code_for_node(orig_mod, ol.body)
                m_b = code_for_node(mut_mod, mut_col.lambdas[idx].body)
                if (o_b == "None" and m_b == "0") or (o_b == "0" and m_b == "None"):
                    ops.append("operator_lambda"); evidence_parts.append(f"lambda {o_b}->{m_b}")
            except Exception:
                continue

    # dict keyword mutated with 'XX'
    for oc in orig_col.calls:
        for mc in mut_col.calls:
            try:
                fo = code_for_node(orig_mod, oc.func)
            except Exception:
                fo = ""
            if fo.endswith("dict") or fo == "dict":
                kws = [a.keyword.value if a.keyword else None for a in mc.args]
                if any(kw and "XX" in kw for kw in kws):
                    ops.append("operator_dict_arguments"); evidence_parts.append("dict kw contains 'XX'")

    # arg removal or arg->None
    for oc in orig_col.calls:
        for mc in mut_col.calls:
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

    for oc, mc in zip(orig_col.calls, mut_col.calls):
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
    for ou in orig_col.unarys:
        try:
            if isinstance(ou.operator, (cst.Not, cst.BitInvert)):
                orepr = code_for_node(orig_mod, ou.expression)
                found = any(code_for_node(mut_mod, mu.expression) == orepr for mu in mut_col.unarys)
                if not found:
                    ops.append("operator_remove_unary_ops"); evidence_parts.append(f"unary removed {orepr}")
        except Exception:
            continue

    # keywords (is/in swaps)
    for oc in orig_col.comparisons:
        for mc in mut_col.comparisons:
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
    for on in orig_col.names:
        for mn in mut_col.names:
            try:
                if on.value != mn.value:
                    if {on.value, mn.value} == {"True","False"}:
                        ops.append("operator_name"); evidence_parts.append("True<->False")
                    elif on.value == "deepcopy" and mn.value == "copy":
                        ops.append("operator_name"); evidence_parts.append("deepcopy->copy")
            except Exception:
                pass

    # operator swap for binary ops
    for ob, mb in zip(orig_col.binary_ops, mut_col.binary_ops):
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
    for om in orig_col.matches:
        for mm in mut_col.matches:
            if len(mm.cases) < len(om.cases):
                ops.append("operator_match"); evidence_parts.append(f"match cases {len(om.cases)}->{len(mm.cases)}")

    for osub, msub in zip(orig_col.subscripts, mut_col.subscripts):
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

def process_file(path: str) -> List[Dict]:
    mutants, defs = parse_log_file(path)
    rows: List[Dict] = []
    defs_items_rev = list(defs.items())[::-1]
    for mname, info in mutants.items():
        mut_src = info.get("mut_src", "")
        trace = info.get("trace", "")
        status = info.get("status", "")
        orig_src = None

        mo = re.match(r"(?P<base>.+)__mutmut_\d+$", mname)
        if mo:
            candidate = mo.group("base") + "__mutmut_orig"
            if candidate in defs:
                orig_src = defs[candidate]
            else:
                for name, src in defs_items_rev:
                    if name == candidate:
                        orig_src = src; break
                if not orig_src:
                    for name, src in defs_items_rev:
                        if name.endswith("__mutmut_orig") and mo.group("base") in name:
                            orig_src = src; break

        if not orig_src:
            for name, src in defs_items_rev:
                if name.endswith("__mutmut_orig"):
                    orig_src = src
                    break

        if not orig_src:
            detected = ["_simple_mutation_mapping"]
            confidence = "low"
            evidence = "original not found in same log file"
        else:
            detected, confidence, evidence_parts = detect_operators_from_pair(orig_src, mut_src, trace)
            if evidence_parts:
                evidence = "; ".join(evidence_parts)
            else:
                te = choose_trace_evidence(trace)
                if te:
                    evidence = te
                else:
                    evidence = (mut_src.strip().splitlines()[0] if mut_src.strip() else "no-evidence")
        rows.append({
            "source_log": path,
            "mutant": mname,
            "status": status,
            "operators": ";".join(detected),
            "confidence": confidence,
            "evidence": evidence,
        })
    return rows

def run_and_write(input_path: str, out_csv: str):
    import os
    all_rows: List[Dict] = []
    if os.path.isdir(input_path):
        for fname in sorted(os.listdir(input_path)):
            if not fname.endswith(".log"): continue
            full = os.path.join(input_path, fname)
            try:
                all_rows.extend(process_file(full))
            except Exception as e:
                all_rows.append({
                    "source_log": full,
                    "mutant": "<PARSING_ERROR>",
                    "status": "ERROR",
                    "operators": "_simple_mutation_mapping",
                    "confidence": "low",
                    "evidence": f"failed to parse: {e}",
                })
    else:
        try:
            all_rows = process_file(input_path)
        except Exception as e:
            all_rows = [{
                "source_log": input_path,
                "mutant": "<PARSING_ERROR>",
                "status": "ERROR",
                "operators": "_simple_mutation_mapping",
                "confidence": "low",
                "evidence": f"failed to parse: {e}",
            }]

    fieldnames = ["source_log","mutant","status","operators","confidence","evidence"]
    try:
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in all_rows:
                writer.writerow(r)
        print(f"Wrote CSV to {out_csv}", file=sys.stderr)
    except Exception as e:
        raise RuntimeError(f"Failed to write CSV {out_csv}: {e}")

def main():
    print(f"Input: {INPUT_PATH}", file=sys.stderr)
    print(f"Output: {OUT_CSV}", file=sys.stderr)
    run_and_write(INPUT_PATH, OUT_CSV)

if __name__ == "__main__":
    main()
