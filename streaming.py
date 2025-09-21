from openai import OpenAI
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)

with client.responses.stream(
    model=MODEL,
    input="200文字で自己紹介をストリーム出力してください。"
) as stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
        elif event.type == "response.error":
            print("\nError:", event.error)
    final = stream.get_final_response()
    print("\n---\nFinal:", final.output_text)