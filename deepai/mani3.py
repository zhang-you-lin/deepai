import os
from openai import OpenAI

client = OpenAI(
     api_key="45022cbd3b7bf69e8e25f08f7460c653314daee8",  # 含有 AI Studio 访问令牌的环境变量，https://aistudio.baidu.com/account/accessToken,
     base_url="https://aistudio.baidu.com/llm/lmapi/v3",  # aistudio 大模型 api 服务域名
)

chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'system', 'content': '你是 AI Studio 实训AI开发平台的开发者助理，你精通开发相关的知识，负责给开发者提供搜索帮助建议。'},
        {'role': 'user', 'content': '输出99乘法表'}
    ],
    model="ernie-3.5-8k",
    stream=True,
)

#
# print(chat_completion.choices[0].message.content)

#流式输出
for chunk in chat_completion:
    print(chunk.choices[0].delta.content or "", end="")