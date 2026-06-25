#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日站会简报生成脚本 — 自动汇总项目状态，生成站会简报
Project Singularity

用法: python daily_brief.py
输出: 控制台打印 + 07_Team/daily_briefs/YYYY-MM-DD.md
"""

import re
import csv
import json
from pathlib import Path
from datetime import datetime

# ==================== 配置区 ====================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHECKLIST_FILE = PROJECT_ROOT / "项目进度检查清单.md"
QUEUE_FILE = PROJECT_ROOT / "06_Research" / "render_queue.json"
GEN_LOG_FILE = PROJECT_ROOT / "06_Research" / "video_gen_log.csv"
FAILURE_LOG_FILE = PROJECT_ROOT / "06_Research" / "失败案例记录表.md"
BRIEF_DIR = PROJECT_ROOT / "07_Team" / "daily_briefs"

# ==================== 工具函数 ====================


def parse_checklist(filepath: Path) -> dict:
    """解析检查清单。"""
    if not filepath.exists():
        return {}

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    sections = {}
    current_section = None
    for line in content.split("\n"):
        section_match = re.match(r"^##+\s+(.+)", line)
        if section_match:
            current_section = section_match.group(1).strip()
            sections[current_section] = {"total": 0, "done": 0, "pending": []}
            continue
        if current_section:
            if re.match(r"^\s*- \[x\]", line):
                sections[current_section]["total"] += 1
                sections[current_section]["done"] += 1
            elif re.match(r"^\s*- \[ \]", line):
                sections[current_section]["total"] += 1
                # 提取任务描述
                task_text = re.sub(r"^\s*- \[ \]\s*", "", line).strip()
                if task_text:
                    sections[current_section]["pending"].append(task_text)
    return sections


def parse_render_queue(filepath: Path) -> dict:
    """解析渲染队列。"""
    if not filepath.exists():
        return {"pending": 0, "running": 0, "completed": 0, "failed": 0}
    with open(filepath, "r", encoding="utf-8") as f:
        queue = json.load(f)
    pending = len([t for t in queue.get("tasks", []) if t.get("status") == "pending"])
    running = len([t for t in queue.get("tasks", []) if t.get("status") == "running"])
    completed = len(queue.get("completed", []))
    failed = len(queue.get("failed", []))
    return {"pending": pending, "running": running, "completed": completed, "failed": failed}


def parse_gen_log(filepath: Path) -> dict:
    """解析视频生成日志。"""
    if not filepath.exists():
        return {"total": 0, "success": 0, "failed": 0, "skipped": 0}
    total = success = failed = skipped = 0
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            status = row.get("status", "")
            if status == "success":
                success += 1
            elif status == "failed":
                failed += 1
            elif status == "skipped":
                skipped += 1
    return {"total": total, "success": success, "failed": failed, "skipped": skipped}


def count_assets() -> dict:
    """统计当前资产数量。"""
    assets = {}
    # 关键帧
    scene_dir = PROJECT_ROOT / "01_Assets" / "Scenes"
    assets["keyframes"] = len(list(scene_dir.glob("*.png"))) if scene_dir.exists() else 0
    # 视频
    video_dir = PROJECT_ROOT / "05_Output" / "Rough_Cuts"
    video_exts = {".mp4", ".avi", ".mov", ".mkv", ".webm"}
    assets["videos"] = len([f for f in video_dir.rglob("*") if f.suffix.lower() in video_exts]) if video_dir.exists() else 0
    # 音频
    audio_dir = PROJECT_ROOT / "01_Assets" / "Audio"
    audio_exts = {".wav", ".mp3"}
    assets["audio"] = len([f for f in audio_dir.rglob("*") if f.suffix.lower() in audio_exts]) if audio_dir.exists() else 0
    # 最终成片
    final_dir = PROJECT_ROOT / "05_Output" / "Final"
    assets["final"] = len([f for f in final_dir.rglob("*") if f.suffix.lower() in video_exts]) if final_dir.exists() else 0
    return assets


# ==================== 主流程 ====================


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("=" * 60)
    print(f"  Project Singularity — 每日站会简报")
    print(f"  日期: {today}")
    print("=" * 60)

    # 1. 检查清单进度
    checklist = parse_checklist(CHECKLIST_FILE)
    total_done = sum(s["done"] for s in checklist.values())
    total_tasks = sum(s["total"] for s in checklist.values())
    overall_pct = (total_done / total_tasks * 100) if total_tasks > 0 else 0

    # 2. 渲染队列
    queue = parse_render_queue(QUEUE_FILE)

    # 3. 生成日志
    gen_log = parse_gen_log(GEN_LOG_FILE)

    # 4. 资产统计
    assets = count_assets()

    # 5. 待办任务（取检查清单中未完成项）
    all_pending = []
    for section, stats in checklist.items():
        for task in stats.get("pending", []):
            all_pending.append((section, task))

    # 生成简报文本
    brief = []
    brief.append(f"# 每日站会简报 — {today}\n")
    brief.append(f"> 生成时间: {now_str}\n")

    # 整体进度
    brief.append("## 一、整体进度\n")
    bar_len = 30
    filled = int(bar_len * overall_pct / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    brief.append(f"```\n{bar} {overall_pct:.1f}% ({total_done}/{total_tasks})\n```\n")

    # 各阶段进度
    brief.append("## 二、各阶段进度\n")
    brief.append("| 阶段 | 完成 | 总数 | 进度 |")
    brief.append("|------|------|------|------|")
    for section, stats in checklist.items():
        pct = (stats["done"] / stats["total"] * 100) if stats["total"] > 0 else 0
        brief.append(f"| {section} | {stats['done']} | {stats['total']} | {pct:.0f}% |")
    brief.append("")

    # 资产统计
    brief.append("## 三、资产统计\n")
    brief.append("| 资产类型 | 当前数量 | 目标 | 状态 |")
    brief.append("|----------|----------|------|------|")
    brief.append(f"| 场景关键帧 | {assets['keyframes']} | 29 | {'✅' if assets['keyframes'] >= 29 else '⏳'} |")
    brief.append(f"| 原始视频 | {assets['videos']} | 24 | {'✅' if assets['videos'] >= 24 else '⏳'} |")
    brief.append(f"| 音频素材 | {assets['audio']} | 15+ | {'✅' if assets['audio'] >= 15 else '⏳'} |")
    brief.append(f"| 最终成片 | {assets['final']} | 1 | {'✅' if assets['final'] >= 1 else '⏳'} |")
    brief.append("")

    # 渲染队列
    brief.append("## 四、渲染队列\n")
    brief.append(f"- 待执行: {queue['pending']}")
    brief.append(f"- 执行中: {queue['running']}")
    brief.append(f"- 已完成: {queue['completed']}")
    brief.append(f"- 已失败: {queue['failed']}")
    brief.append("")

    # 生成日志
    if gen_log["total"] > 0:
        brief.append("## 五、生成日志\n")
        brief.append(f"- 总任务: {gen_log['total']}")
        brief.append(f"- 成功: {gen_log['success']}")
        brief.append(f"- 失败: {gen_log['failed']}")
        brief.append(f"- 跳过: {gen_log['skipped']}")
        success_rate = gen_log["success"] / gen_log["total"] * 100 if gen_log["total"] > 0 else 0
        brief.append(f"- 成功率: {success_rate:.1f}%")
        brief.append("")

    # 今日待办（取前 10 项未完成任务）
    brief.append("## 六、今日待办（优先）\n")
    if all_pending:
        for i, (section, task) in enumerate(all_pending[:10], 1):
            brief.append(f"{i}. [{section}] {task}")
        if len(all_pending) > 10:
            brief.append(f"\n... 还有 {len(all_pending) - 10} 项待办")
    else:
        brief.append("所有任务已完成！🎉")
    brief.append("")

    # 站会模板
    brief.append("## 七、站会发言模板\n")
    brief.append("```")
    brief.append("昨日完成:")
    brief.append("  - [填写完成的任务]")
    brief.append("")
    brief.append("今日计划:")
    brief.append("  - [填写今日计划]")
    brief.append("")
    brief.append("阻塞/风险:")
    brief.append("  - [填写阻塞项，无则填'无']")
    brief.append("```")
    brief.append("")

    brief_text = "\n".join(brief)

    # 打印到控制台
    print(brief_text)

    # 保存文件
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    brief_file = BRIEF_DIR / f"{today}.md"
    with open(brief_file, "w", encoding="utf-8") as f:
        f.write(brief_text)

    print(f"\n{'='*60}")
    print(f"  简报已保存: {brief_file}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
