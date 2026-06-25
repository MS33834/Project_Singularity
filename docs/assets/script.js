const translations = {
  en: {
    nav_about: "About",
    nav_pipeline: "Pipeline",
    nav_repos: "Repos",
    nav_start: "Start",
    hero_eyebrow: "AIGC video production pipeline",
    hero_title: "From script to 4K master, repeatable.",
    hero_lead:
      "Project Singularity is a workflow template for making 3–5 minute AIGC short films. " +
      "It includes scripts, storyboards, ComfyUI workflows, automation scripts, and a worked example: " +
      "the sci-fi micro-short <em>Echo of the Singularity</em>.",
    hero_cta_primary: "View on GitHub",
    hero_cta_secondary: "View on GitCode",
    about_title: "What this project is",
    about_p1:
      "Making an AIGC video is easy for a five-second clip. At three to five minutes, things fall apart: " +
      "characters look different shot to shot, prompts drift, parameters get lost, and teams step on each other’s work.",
    about_p2:
      "This repository bundles the documents, scripts, and workflows we use to keep production sane. " +
      "It is not a magic button. It is a structured way to plan, generate, check, and deliver.",
    feature_1_title: "Locked characters",
    feature_1_text: "Flux.1 Kontext + IPAdapter keep the lead character consistent across all 24 shots.",
    feature_2_title: "Hybrid generation",
    feature_2_text: "Standard shots run locally on Wan2.2 I2V; complex moves use Kling 2.5 Turbo with start/end frames.",
    feature_3_title: "Tracked production",
    feature_3_text: "Shot tracker, render queue, daily briefs, and QA checklists keep everyone aligned.",
    feature_4_title: "Full post pipeline",
    feature_4_text: "DaVinci edit and color, ElevenLabs dialogue, Suno music, Topaz 4K upscale.",
    pipeline_title: "Pipeline overview",
    step_1_title: "Plan",
    step_1_text: "Script, world-building, character bible, and 24-shot storyboard.",
    step_2_title: "Assets",
    step_2_text: "Reference images, keyframes, and locked prompts for every shot.",
    step_3_title: "Motion",
    step_3_text: "Batch video generation with seed tracking and quality checks.",
    step_4_title: "Post",
    step_4_text: "Edit, sound design, music, color grade, and 4K delivery.",
    step_5_title: "Release",
    step_5_text: "Packaged workflows, tutorial, and release checklist.",
    repos_title: "Repository mirrors",
    repos_text: "The project is mirrored between GitHub and GitCode. Both stay in sync via an automation script.",
    start_title: "Quick start",
    start_1: "Clone the repository and install Python dependencies with <code>make setup</code>.",
    start_2: "Read <code>AIGC_Experience_Chain.md</code> to understand the full workflow.",
    start_3: "Explore the <code>examples/奇点回响/</code> case study for a worked production plan.",
    start_4: "Run <code>make check</code> to verify the project structure.",
    start_5: "Open the ComfyUI workflows in <code>03_Workflows/</code> and adapt them to your project.",
    footer: "Project Singularity — maintained by the team. Released under the MIT License.",
  },
  zh: {
    nav_about: "关于",
    nav_pipeline: "流程",
    nav_repos: "仓库",
    nav_start: "开始",
    hero_eyebrow: "AIGC 视频生产管线",
    hero_title: "从剧本到 4K 母版，可复现。",
    hero_lead:
      "Project Singularity 是一套用于制作 3–5 分钟 AIGC 短片的流程模板。 " +
      "它包含剧本、分镜、ComfyUI 工作流、自动化脚本，以及一个完整示例：科幻微短剧《奇点回响》。",
    hero_cta_primary: "在 GitHub 查看",
    hero_cta_secondary: "在 GitCode 查看",
    about_title: "这个项目是什么",
    about_p1:
      "做一个五秒钟的 AIGC 视频很容易。拉长到三五分钟，问题会集中爆发： " +
      "角色每镜长得不一样、提示词漂移、参数丢失、团队协作互相踩脚。",
    about_p2:
      "这个仓库把我们在实际制作中用来保持理智的文档、脚本和工作流打包在一起。 " +
      "它不是魔法按钮，而是一种结构化的规划、生成、检查与交付方式。",
    feature_1_title: "锁定角色",
    feature_1_text: "Flux.1 Kontext + IPAdapter 让主角在全部 24 镜中保持一致。",
    feature_2_title: "混合生成",
    feature_2_text: "标准镜头本地 Wan2.2 I2V；复杂运镜用可灵 2.5 Turbo 首尾帧约束。",
    feature_3_title: "可追踪制片",
    feature_3_text: "镜头进度表、渲染队列、日报和 QA 清单让团队保持同步。",
    feature_4_title: "完整后期管线",
    feature_4_text: "达芬奇剪辑调色、ElevenLabs 对白、Suno 配乐、Topaz 4K 超分。",
    pipeline_title: "流程概览",
    step_1_title: "策划",
    step_1_text: "剧本、世界观、角色圣经与 24 镜分镜表。",
    step_2_title: "资产",
    step_2_text: "参考图、关键帧，以及每镜的锁定提示词。",
    step_3_title: "动态",
    step_3_text: "批量视频生成，记录 seed 并做质量检查。",
    step_4_title: "后期",
    step_4_text: "剪辑、音效、音乐、调色与 4K 交付。",
    step_5_title: "发布",
    step_5_text: "打包工作流、教程与发布检查清单。",
    repos_title: "仓库镜像",
    repos_text: "项目在 GitHub 与 GitCode 双仓库镜像，通过自动化脚本保持同步。",
    start_title: "快速开始",
    start_1: "克隆仓库，使用 <code>make setup</code> 安装 Python 依赖。",
    start_2: "阅读 <code>AIGC_Experience_Chain.md</code> 了解完整工作流。",
    start_3: "浏览 <code>examples/奇点回响/</code> 案例研究，参考完整制作计划。",
    start_4: "运行 <code>make check</code> 验证项目结构。",
    start_5: "打开 <code>03_Workflows/</code> 中的 ComfyUI 工作流，按需改造。",
    footer: "Project Singularity — 由项目团队维护。基于 MIT 许可证发布。",
  },
};

function setLanguage(lang) {
  document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const text = translations[lang][key];
    if (text !== undefined) {
      el.innerHTML = text;
    }
  });
  localStorage.setItem("ps-lang", lang);
  const toggle = document.getElementById("lang-toggle");
  if (toggle) {
    toggle.textContent = lang === "en" ? "中文" : "English";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const saved = localStorage.getItem("ps-lang");
  const initial = saved === "zh" ? "zh" : "en";
  setLanguage(initial);

  const toggle = document.getElementById("lang-toggle");
  if (toggle) {
    toggle.addEventListener("click", () => {
      const current = document.documentElement.lang.startsWith("zh") ? "zh" : "en";
      setLanguage(current === "en" ? "zh" : "en");
    });
  }
});
