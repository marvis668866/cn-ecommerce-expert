import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

def load_system_prompt():
    # Attempt to read SKILL.md from the parent directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_path = os.path.join(base_dir, 'SKILL.md')
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "You are an E-commerce Expert."

def load_template(template_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'resources', f'{template_name}.md')
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        print("❌ 错误 (Error): 缺少 OPENAI_API_KEY。请在当前目录创建 .env 文件并填入您的 API 密钥。")
        sys.exit(1)
    
    # Initialize the OpenAI client (can point to any OpenAI-compatible endpoint)
    client = OpenAI(api_key=api_key, base_url=base_url)

    print("==================================================")
    print("🛒 国内电商运营专家 (CN E-commerce Expert) SDK 初始化成功！")
    print("==================================================\n")

    product_name = input("👉 请输入您要策划的产品名称 (例如: 氨基酸洗面奶): ")
    task_type = input("👉 请输入您需要的任务 (1: Listing优化, 2: 活动策划, 3: 综合建议): ")

    system_prompt = load_system_prompt()
    user_prompt = f"我的产品是：{product_name}。\n"

    if "1" in task_type or "Listing" in task_type:
        template = load_template("product_listing")
        user_prompt += f"请帮我完成一份高转化的 Listing 策划案。请严格参考以下模板结构输出：\n\n{template}"
    elif "2" in task_type or "活动" in task_type:
        template = load_template("campaign_plan")
        user_prompt += f"请帮我完成一份大促活动策划案。请严格参考以下模板结构输出：\n\n{template}"
    else:
        user_prompt += "请运用您的专业知识，结合市场现状，为我的产品提供详细的运营策略与起盘建议。"

    print("\n⏳ 专家正在思考中，请耐心等待 (约需十余秒)...\n")

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        
        result = response.choices[0].message.content
        print("✅ 策划方案已生成：\n")
        print(result)

        # Save to file
        output_file = f"{product_name}_运营方案.md".replace(" ", "_")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n📁 方案已自动保存为当前目录下的: {output_file}")

    except Exception as e:
        print(f"❌ 调用大模型时发生错误: {e}")

if __name__ == "__main__":
    main()
