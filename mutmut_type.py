#!/usr/bin/env python3
import subprocess
import re

def get_mutant_type(mutant_name):
    """
    解析 mutmut show 输出，判断突变体类型
    """
    try:
        diff_text = subprocess.check_output(["mutmut", "show", mutant_name], text=True)
    except subprocess.CalledProcessError:
        return "unknown"

    code = diff_text.replace(" ", "").replace("\n", "")

    # 1. None / Null assignment
    if re.search(r'=(None)', code):
        return "None Assignment"

    # 2. Boundary change (循环边界修改或 low/high 增减)
    if re.search(r'whilelow<high', code) or re.search(r'low\+=[0-9]+', code) or re.search(r'high-=[0-9]+', code):
        return "Boundary Change"

    # 3. Arithmetic Operator Replacement (AOR)
    if re.search(r'return[+-]?\(low[+-][0-9]+\)', code) or re.search(r'[+\-*/%]', code):
        return "Arithmetic Operator Replacement"

    # 4. Division / Floor division change
    if re.search(r'mid=\(low\+high\)/2', code):
        return "Division Replacement"
    if re.search(r'mid=\(low\+high\)//2', code):
        return "Floor Division"

    # 5. Comparison replacement
    if re.search(r'midVal[<>]=key', code) or re.search(r'midVal[<>=!]=midVal', code):
        return "Comparison Replacement"

    # 6. Boolean replacement
    if "True" in diff_text or "False" in diff_text:
        return "Boolean Replacement"

    # fallback
    return "Line Change"


def main():
    # 自动获取所有突变体名称
    try:
        output = subprocess.check_output(["mutmut", "results"], text=True)
    except subprocess.CalledProcessError:
        print("Error: cannot get mutmut results")
        return

    mutant_names = [line.split(":")[0].strip() for line in output.strip().splitlines() if line.strip()]

    # 输出每个突变体及类型
    for mutant in mutant_names:
        typ = get_mutant_type(mutant)
        print(f"{mutant}: {typ}")


if __name__ == "__main__":
    main()
