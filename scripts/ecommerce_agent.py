import os
import sys
import time
from openai import OpenAI
from dotenv import load_dotenv

def load_system_prompt():
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

def generate_plan(client, product_name, task_type, system_prompt):
    user_prompt = f"我的产品是：{product_name}。\n"

    if "1" in task_type or "Listing" in task_type:
        template = load_template("product_listing")
        user_prompt += f"请帮我完成一份高转化的 Listing 策划案。请严格参考以下模板结构输出：\n\n{template}"
    elif "2" in task_type or "活动" in task_type:
        template = load_template("campaign_plan")
        user_prompt += f"请帮我完成一份大促活动策划案。请严格参考以下模板结构输出：\n\n{template}"
    else:
        user_prompt += "请运用您的专业知识，结合市场现状，为我的产品提供详细的运营策略与起盘建议。"

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        print("❌ 错误 (Error): 缺少 OPENAI_API_KEY。请在当前目录创建 .env 文件并填入您的 API 密钥。")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key, base_url=base_url)

    print("==================================================")
    print("🛒 国内电商运营专家 (CN E-commerce Expert) SDK 初始化成功！")
    print("==================================================\n")

    mode = input("👉 请选择运行模式 (1: 单个商品处理, 2: 批量文件处理 [Batch Processing]): ")
    system_prompt = load_system_prompt()
    task_type = input("👉 请输入您需要的任务 (1: Listing优化, 2: 活动策划, 3: 综合建议): ")

    if mode == "1":
        product_name = input("👉 请输入您要策划的产品名称 (例如: 氨基酸洗面奶): ")
        print("\n⏳ 专家正在思考中，请耐心等待...\n")
        try:
            result = generate_plan(client, product_name, task_type, system_prompt)
            print("✅ 策划方案已生成：\n")
            print(result)
            output_file = f"{product_name}_运营方案.md".replace(" ", "_")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"\n📁 方案已自动保存为当前目录下的: {output_file}")
        except Exception as e:
            print(f"❌ 发生错误: {e}")

    elif mode == "2":
        file_path = input("👉 请输入包含商品名称的文本文件路径 (例如: products.txt，每行一个商品): ")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                products = [line.strip() for line in f if line.strip()]
            
            print(f"\n📦 共读取到 {len(products)} 个商品，开始批量生成...\n")
            
            os.makedirs("batch_outputs", exist_ok=True)
            for i, product_name in enumerate(products):
                print(f"[{i+1}/{len(products)}] 正在处理: {product_name}...")
                try:
                    result = generate_plan(client, product_name, task_type, system_prompt)
                    output_file = os.path.join("batch_outputs", f"{product_name}_运营方案.md".replace(" ", "_").replace("/", "_"))
                    with open(output_file, 'w', encoding='utf-8') as out_f:
                        out_f.write(result)
                    print(f"   ✅ 完成，已保存至 {output_file}")
                    time.sleep(1) # Rate limiting prevention
                except Exception as e:
                    print(f"   ❌ 处理 {product_name} 时失败: {e}")
            print("\n🎉 批量处理全部完成！结果已保存在 batch_outputs/ 文件夹中。")
        except FileNotFoundError:
            print(f"❌ 找不到文件: {file_path}")
    else:
        print("❌ 无效的模式选择。")

if __name__ == "__main__":
    main()
