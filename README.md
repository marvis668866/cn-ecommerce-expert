# 🛒 CN E-commerce Expert (AI Agent Skill) / 国内电商运营专家

![Stars](https://img.shields.io/github/stars/marvis668866/cn-ecommerce-expert?style=for-the-badge&color=yellow)
![Forks](https://img.shields.io/github/forks/marvis668866/cn-ecommerce-expert?style=for-the-badge&color=blue)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Agents](https://img.shields.io/badge/Supported_Agents-Antigravity_|_Claude_Code_|_Codex_|_Workbuddy_|_Cursor-purple?style=for-the-badge)

[English](#english) | [中文](#chinese)

<a name="english"></a>
## 🚀 Universal AI Agent Skill for Chinese E-commerce

This is a universal custom **Skill / Prompt Engineering Package** designed for advanced AI Agents (including **Google Antigravity, Claude Code, Codex, Workbuddy, Cursor**, etc.). 

By installing this skill, your AI assistant will instantly transform into a **Senior Chinese E-commerce Operations Director** with 10+ years of experience, mastering the underlying logic of platforms like Taobao, Tmall, JD.com, Douyin (TikTok China), and Xiaohongshu (RED).

### 🌟 Core Features
*   **Market & Competitor Analysis**: Deep competitor teardowns and trend insights based on platform characteristics.
*   **High-Conversion Listings**: SEO-optimized titles, pain-point-driven selling points, and product description copywriting.
*   **Full-Cycle Campaign Planning**: End-to-end marketing rhythms and strategies for major festivals like "Double 11" and "618".
*   **Data-Driven Diagnostics**: Precise identification of traffic, CVR, and ATV issues with actionable optimization advice.
*   **[NEW] Batch Processing Automation**: The Python SDK now supports reading `.txt` or `.csv` files to automatically generate hundreds of e-commerce operation plans asynchronously.

### 📦 Installation

**For Google Antigravity Users:**
```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/marvis668866/cn-ecommerce-expert.git ~/.gemini/config/skills/cn-ecommerce-expert
```

**For Claude Code / Codex / Workbuddy / Cursor Users:**
Simply clone this repository into your project's local agent skills directory (e.g., `.agents/skills/` or `.cursor/rules/`), or directly feed the `SKILL.md` content to your AI agent as system instructions.

**👨‍💻 For Python Developers (Standalone Script):**
We also provide a standalone Python script that automates the prompt generation using the OpenAI API (or any compatible endpoint).
```bash
git clone https://github.com/marvis668866/cn-ecommerce-expert.git
cd cn-ecommerce-expert
pip install -r requirements.txt

# Create a .env file and set OPENAI_API_KEY
echo "OPENAI_API_KEY=your_key_here" > .env
python scripts/ecommerce_agent.py
```

---

<a name="chinese"></a>
## 🚀 国内电商运营专家 (通用 AI 智能体技能)

这是一个为高级 AI 智能体（包括 **Google Antigravity, Claude Code, Codex, Workbuddy, Cursor** 等）打造的通用自定义技能包。

安装此技能后，您的 AI 助手将化身为拥有 10 年操盘经验的**国内全栈电商运营总监**，精通淘宝、天猫、京东、抖音、小红书等平台的底层逻辑。

### 🌟 核心功能
*   **市场与竞品分析**：基于平台特性的深度竞品拆解与趋势洞察。
*   **高转化 Listing 打造**：符合 SEO 逻辑的标题优化、痛点驱动的卖点提炼与详情页文案。
*   **全周期活动策划**：从 618 到双 11，覆盖蓄水到爆发的完整营销节奏与玩法。
*   **数据驱动复盘**：精准定位流量、转化率、客单价问题，并给出实操改进建议。
*   **[NEW] 批量自动化引擎**：Python SDK 现已支持读取外部 `.txt` 文件，一键为成百上千个 SKU 自动生成策划案并归档。

### 📦 安装方法

**对于 Google Antigravity 用户：**
```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/marvis668866/cn-ecommerce-expert.git ~/.gemini/config/skills/cn-ecommerce-expert
```

**对于 Claude Code / Codex / Workbuddy / Cursor 等其他智能体用户：**
只需将此仓库克隆到您项目的自定义规则或技能目录下（例如 `.agents/skills/` 或 `.cursor/rules/`），或者直接将 `SKILL.md` 喂给您的 AI 作为系统级指令即可。

**👨‍💻 给开发者的独立 Python 脚本：**
本仓库还提供了一个可以直接运行的 Python 脚本，支持通过 OpenAI API (或其他兼容的国产大模型接口) 一键全自动调用该技能包。
```bash
git clone https://github.com/marvis668866/cn-ecommerce-expert.git
cd cn-ecommerce-expert
pip install -r requirements.txt

# 创建 .env 文件并填入您的 API Key
echo "OPENAI_API_KEY=your_key_here" > .env
python scripts/ecommerce_agent.py
```
