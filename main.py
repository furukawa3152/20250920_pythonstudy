from openai import OpenAI
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)

response = client.responses.create(
    model=MODEL,
    input="日本語で、このSDKの最短使用例を1行で説明して。"
)

print(response.output_text)