import os
from openai import OpenAI

def get_response(messages):
    client = OpenAI(
        api_key="45022cbd3b7bf69e8e25f08f7460c653314daee8",  # 含有 AI Studio 访问令牌的环境变量，https://aistudio.baidu.com/account/accessToken,
        base_url="https://aistudio.baidu.com/llm/lmapi/v3",  # aistudio 大模型 api 服务域名
    )
    completion = client.chat.completions.create(model="ernie-3.5-8k", messages=messages)
    return completion

messages = [
    {
        "role": "system",
        "content": "你是 AI Studio 开发者助理，你精通开发相关的知识，负责给开发者提供搜索帮助建议。",
    }
]

assistant_output = "您好，我是AI Studio 开发者助理，请问有什么能帮助你的吗？"
print(f"""输入："结束"，结束对话\n""")
print(f"模型输出：{assistant_output}\n")
user_input = ""
while "结束" not in user_input:
    user_input = input("请输入：")
    # 将用户问题信息添加到messages列表中
    messages.append({"role": "user", "content": user_input})
    assistant_output = get_response(messages).choices[0].message.content
    # 将大模型的回复信息添加到messages列表中
    messages.append({"role": "assistant", "content": assistant_output})
    print(f"模型输出：{assistant_output}")
    print("\n")