# pip install openai
from openai import OpenAI

client = OpenAI(
    api_key="45022cbd3b7bf69e8e25f08f7460c653314daee8",
    base_url="https://api-z8bf7bn9acxfk2x4.aistudio-app.com/v1"
)

completion = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    temperature=0.6,
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    stream=True
)

for chunk in completion:
    if hasattr(chunk.choices[0].delta, "reasoning_content") and chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
    else:
        print(chunk.choices[0].delta.content, end="", flush=True)