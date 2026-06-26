#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Project Singularity — 双仓库同步脚本
# 用法: bash 08_Automation/sync_repos.sh "提交信息"
#
# 功能:
#   1. git add -A
#   2. git commit -m "提交信息"
#   3. git push github main
#   4. git push gitcode main
#
# 安全提示: 不要在 .git/config 或本脚本中硬编码令牌。
#   - HTTPS: 使用 Git 凭据管理器（git config --global credential.helper store/cache）
#   - SSH:   使用 git@github.com:MS33834/Project_Singularity.git
# 仓库地址:
#   GitHub:  https://github.com/MS33834/Project_Singularity
#   GitCode: https://gitcode.com/badhope/Project_Singularity

set -e

cd "$(dirname "$0")/.."

COMMIT_MSG="${1:-update: 同步更新项目进度}"

echo "========================================="
echo "  Project Singularity — 双仓库同步"
echo "========================================="
echo ""

# 1. 检查是否有变更
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "[INFO] 没有变更需要提交"
    exit 0
fi

# 2. 暂存所有变更
echo "[1/4] 暂存变更..."
git add -A
echo "  已暂存文件:"
git status --short | head -20
echo ""

# 3. 提交
echo "[2/4] 提交..."
git commit -m "$COMMIT_MSG"
echo ""

# 4. 推送到 GitHub
echo "[3/4] 推送到 GitHub (MS33834/Project_Singularity)..."
if git push github main 2>&1; then
    echo "  [OK] GitHub 推送成功"
else
    echo "  [FAIL] GitHub 推送失败"
    exit 1
fi
echo ""

# 5. 推送到 GitCode
echo "[4/4] 推送到 GitCode (badhope/Project_Singularity)..."
if git push gitcode main 2>&1; then
    echo "  [OK] GitCode 推送成功"
else
    echo "  [FAIL] GitCode 推送失败"
    exit 1
fi

echo ""
echo "========================================="
echo "  同步完成!"
echo "  GitHub:  https://github.com/MS33834/Project_Singularity"
echo "  GitCode: https://gitcode.com/badhope/Project_Singularity"
echo "========================================="
