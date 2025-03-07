import os
from openai import OpenAI

client = OpenAI(
     api_key="45022cbd3b7bf69e8e25f08f7460c653314daee8",  # 含有 AI Studio 访问令牌的环境变量，https://aistudio.baidu.com/account/accessToken,
     base_url="https://aistudio.baidu.com/llm/lmapi/v3",  # aistudio 大模型 api 服务域名
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': '写一首关于春天的诗'
        }
    ],
    model="ernie-3.5-8k",
    temperature=0.99,  # 控制随机性，取值范围(0, 1.0]，默认0.95，值越大输出更随机
    top_p=0.99,  # 控制多样性，取值范围[0, 1.0]，默认0.7，值越大生成文本的多样性越强
    frequency_penalty=0.0,  # 词频惩罚系数：值越大，模型越倾向于使用低频词，避免重复使用同一个词。取值范围[-2.0, 2.0]
    presence_penalty=0.0,  # 存在惩罚系数：值越大，模型越倾向于使用新的词，避免话题重复。取值范围[-2.0, 2.0]
    stop=["停止"],  # 生成停止标识符，最多4个，每个长度不超过20字符
    seed=123456766,  # 随机种子，取值范围(0, 2147483647)，用于生成复现
    response_format={ "type": "text" },  # 指定返回文本格式，可选text或json_object
    extra_body={
        "penalty_score": 1.0,  # 重复惩罚系数：通过对已生成的token增加惩罚来减少重复内容，值越大重复越少。取值范围[1.0, 2.0]，默认1.0
        "max_completion_tokens": 2048,  # 最大输出token数，取值范围[2, 2048]
    },
    stream=True,
)

for chunk in chat_completion:
    if hasattr(chunk.choices[0].delta, "reasoning_content") and chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
    else:
        print(chunk.choices[0].delta.content, end="", flush=True)