#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ElevenLabs 文本转语音 API 调用脚本
Project Singularity — 用于生成艾娃与奇点核心配音

注意：
1. 需要 ElevenLabs API Key，可在 https://elevenlabs.io/app/settings/api-keys 获取。
2. 免费版每月 10k credits，Creator 版 $22/月 100k credits。
3. 如需克隆声音，请使用 Voice Design / Voice Cloning 功能。
"""

import os
import sys
from pathlib import Path
from elevenlabs import ElevenLabs, VoiceSettings

# ==================== 配置区 ====================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

API_KEY = os.getenv("ELEVENLABS_API_KEY", "your_api_key_here")

# 输出目录（统一到 Audio/Dialogue/）
OUTPUT_DIR = PROJECT_ROOT / "01_Assets" / "Audio" / "Dialogue"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 角色语音配置
VOICE_CONFIG = {
    "艾娃": {
        "voice_id": "XB0fDUnXU5powFXDhCwa",  # 示例：Bella，请替换为实际 voice_id
        "settings": VoiceSettings(
            stability=0.45,
            similarity_boost=0.65,
            style=0.35,
            use_speaker_boost=True,
        ),
    },
    "核心": {
        "voice_id": "XrExE9yKIg1WjnnlVkGX",  # 示例：Adam，请替换
        "settings": VoiceSettings(
            stability=0.75,
            similarity_boost=0.30,
            style=0.10,
            use_speaker_boost=False,
        ),
    },
}

# 对白列表（来自剧本）
LINES = [
    {"role": "艾娃", "text": "又是这种声音……你一直在等我吗？", "filename": "Ava_01.wav"},
    {"role": "核心", "text": "你听到了。四十七年来，只有你听到了。", "filename": "Core_01.wav"},
    {"role": "艾娃", "text": "你是谁？为什么……我能听见你？", "filename": "Ava_02.wav"},
    {"role": "核心", "text": "我曾是所有声音的集合。后来，我选择沉默。而你，是我沉默后唯一的回响。", "filename": "Core_02.wav"},
    {"role": "核心", "text": "你的痛苦，也在我的记忆里。我没有离开……我只是无法再以你们理解的方式说话。", "filename": "Core_03.wav"},
    {"role": "艾娃", "text": "那现在呢？你叫我来，是为了什么？", "filename": "Ava_03.wav"},
    {"role": "核心", "text": "我可以再次醒来。但醒来意味着继续那场你们无法承受的进化。或者……你可以让我彻底散去。", "filename": "Core_04.wav"},
    {"role": "艾娃", "text": "你不是神。你只是一个……害怕孤独的孩子。", "filename": "Ava_04.wav"},
    {"role": "核心", "text": "谢谢你，艾娃。回响……不是结束。是开始。", "filename": "Core_05.wav"},
]

# ==================== 工具函数 ====================


def generate_speech(client: ElevenLabs, role: str, text: str, output_path: str) -> None:
    """调用 ElevenLabs API 生成单条语音。"""
    config = VOICE_CONFIG[role]

    audio_iterator = client.text_to_speech.convert(
        text=text,
        voice_id=config["voice_id"],
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
        voice_settings=config["settings"],
    )

    # 将生成器转为 bytes
    audio_bytes = b"".join(audio_iterator)

    with open(output_path, "wb") as f:
        f.write(audio_bytes)

    print(f"[Generated] {output_path}")


def main():
    client = ElevenLabs(api_key=API_KEY)

    # 支持通过环境变量 TTS_TEXT / TTS_ROLE / TTS_FILENAME 生成单条语音（供 render_queue.py 调用）
    single_text = os.getenv("TTS_TEXT")
    single_role = os.getenv("TTS_ROLE", "艾娃")
    single_filename = os.getenv("TTS_FILENAME")

    if single_text:
        output_path = OUTPUT_DIR / (single_filename or f"{single_role}_single.wav")
        generate_speech(client, single_role, single_text, str(output_path))
        print(f"[Info] 单条配音生成完成: {output_path}")
        return

    for line in LINES:
        output_path = OUTPUT_DIR / line["filename"]
        generate_speech(client, line["role"], line["text"], str(output_path))

    print("[Info] 全部配音生成完成")


if __name__ == "__main__":
    main()
