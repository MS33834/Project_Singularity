#!/usr/bin/env python3
"""项目结构与健康检查脚本。"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "AIGC_Experience_Chain.md",
    "ROADMAP.md",
    "COST_ANALYSIS.md",
    "TROUBLESHOOTING.md",
    ".env.example",
    "08_Automation/sync_repos.sh",
    "08_Automation/preflight_check.py",
]

REQUIRED_DIRS = [
    "01_Assets",
    "02_Scripts",
    "03_Workflows",
    "04_SOP",
    "05_Output",
    "06_Research",
    "07_Team",
    "08_Automation",
    "09_Release",
    "examples",
]


def check():
    errors = []
    for f in REQUIRED_FILES:
        path = PROJECT_ROOT / f
        if not path.exists():
            errors.append(f"缺失文件: {f}")

    for d in REQUIRED_DIRS:
        path = PROJECT_ROOT / d
        if not path.exists():
            errors.append(f"缺失目录: {d}")

    if errors:
        print("项目健康检查未通过:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("项目健康检查通过。")
    return 0


if __name__ == "__main__":
    sys.exit(check())
