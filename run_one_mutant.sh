#!/usr/bin/env bash
set -euo pipefail

if [ -z "${1-}" ]; then
  echo "Usage: $0 <mutant_name>"
  exit 1
fi

MUTANT_NAME="$1"
TOPDIR="$(pwd)"
TMPDIR="$(mktemp -d --tmpdir run_mutant.XXXXXX)"
LOGDIR="$TOPDIR/pytest_mutant_logs"
mkdir -p "$LOGDIR"

echo "Creating temp copy at $TMPDIR ..."
# 排除 .git、mutants、.mutmut-cache 避免导入冲突与冗余缓存
rsync -a --exclude='.git' --exclude='mutants' --exclude='.mutmut-cache' "$TOPDIR/" "$TMPDIR/"

# 生成 diff（在主项目里）
DIFF_TMP="$(mktemp --tmpdir mutmut_diff.XXXXXX)"
echo "Generating diff for $MUTANT_NAME ..."
mutmut show "$MUTANT_NAME" > "$DIFF_TMP" 2>/dev/null || true
if [ ! -s "$DIFF_TMP" ]; then
  echo "Error: mutmut show produced empty diff for $MUTANT_NAME. Exiting."
  rm -f "$DIFF_TMP"
  rm -rf "$TMPDIR"
  exit 1
fi

cd "$TMPDIR"
export MUTANT_ID="$MUTANT_NAME"

# Apply patch with -p0 then -p1
echo "Applying patch in temp dir..."
if command -v patch >/dev/null 2>&1; then
  if patch -p0 < "$DIFF_TMP" 2>/dev/null; then
    echo "patch -p0 applied"
  elif patch -p1 < "$DIFF_TMP" 2>/dev/null; then
    echo "patch -p1 applied"
  else
    echo "Failed to apply patch with -p0 or -p1. Showing diff head:"
    sed -n '1,120p' "$DIFF_TMP"
    cd "$TOPDIR"
    rm -f "$DIFF_TMP"
    rm -rf "$TMPDIR"
    exit 1
  fi
else
  echo "patch command not found. Install 'patch' or use mutmut.apply in a git repo."
  cd "$TOPDIR"
  rm -f "$DIFF_TMP"
  rm -rf "$TMPDIR"
  exit 1
fi

# 确保临时目录不包含旧的 mutants（双保险）
rm -rf mutants .mutmut-cache || true

# 清理 pycache
find . -name "__pycache__" -exec rm -rf {} + || true
find . -name "*.pyc" -delete || true

echo "Running pytest in temp dir..."
pytest -q --maxfail=1 || true

# save diff as reference
mkdir -p pytest_mutant_logs
cp "$DIFF_TMP" "pytest_mutant_logs/${MUTANT_NAME}.diff.txt" 2>/dev/null || true

# copy generated logs back (if any)
if [ -d pytest_mutant_logs ]; then
  cp -a pytest_mutant_logs/* "$LOGDIR/" 2>/dev/null || true
fi

# cleanup
cd "$TOPDIR"
rm -f "$DIFF_TMP"
rm -rf "$TMPDIR"

echo "Done. Check logs in $LOGDIR"
