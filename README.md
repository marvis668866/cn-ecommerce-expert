# 🛒 国内电商运营专家 (CN E-commerce Expert)

![Stars](https://img.shields.io/github/stars/marvis20260518-sys/cn-ecommerce-expert?style=for-the-badge&color=yellow)
![Forks](https://img.shields.io/github/forks/marvis20260518-sys/cn-ecommerce-expert?style=for-the-badge&color=blue)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Antigravity](https://img.shields.io/badge/Antigravity-Skill-orange?style=for-the-badge)

这是一个为 [Google Antigravity](https://github.com/google/antigravity) 打造的自定义技能 (Skill)。
安装此技能后，您的 AI 助手将化身为拥有 10 年操盘经验的**国内全栈电商运营总监**，精通淘宝、天猫、京东、抖音、小红书等平台的底层逻辑。

## 🌟 核心功能
*   **市场与竞品分析**：基于平台特性的深度竞品拆解与趋势洞察。
*   **高转化 Listing 打造**：符合 SEO 逻辑的标题优化、痛点驱动的卖点提炼与详情页文案。
*   **全周期活动策划**：从 618 到双 11，覆盖蓄水到爆发的完整营销节奏与玩法。
*   **数据驱动复盘**：精准定位流量、转化率、客单价问题，并给出实操改进建议。

## 🚀 安装方法

将此仓库克隆到您的 Antigravity 全局技能目录中：

```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/marvis20260518-sys/cn-ecommerce-expert.git ~/.gemini/config/skills/cn-ecommerce-expert
```

重启或在您的 Antigravity 对话中，该技能即会自动加载。

## 💡 使用示例
在 Antigravity 聊天中，您可以这样向 AI 提问：
*   “我想在淘宝上架一款氨基酸洗面奶，帮我写一个高转化的标题，并提炼主图卖点。”
*   “帮我策划一个抖音小店的‘双11’活动预案，客单价在199元左右。”
*   “近期我的天猫店铺流量没变，但转化率下降了20%，请帮我按电商逻辑进行诊断。”

## 📂 包含的资源模板
本技能内置了以下标准化模板（位于 `resources/` 目录下），AI 会在回答时自动调用：
*   `product_listing.md`: 产品详情页与卖点策划模板
*   `campaign_plan.md`: 大促活动策划执行表
*   `data_review.md`: 店铺数据复盘与诊断报告

## 🤝 贡献
欢迎提交 Pull Request 来完善更多平台的运营策略和 SOP！
