from openai import OpenAI
from openai import AuthenticationError, RateLimitError, APIConnectionError, APIStatusError
from config import API_KEY, MODEL

client = OpenAI(api_key=API_KEY)
try:
    response = client.responses.create(
        model=MODEL,
        input="テスト"
    )
    print(response.output_text)
except AuthenticationError:
    print("認証エラー: APIキーを確認してください。")
except RateLimitError:
    print("レート制限: しばらく待って再試行してください。")
except APIConnectionError:
    print("接続エラー: ネットワークやDNSを確認してください。")
except APIStatusError as e:
    print(f"APIステータスエラー: {e.status_code} {e.response}")
except Exception as e:
    print(f"不明なエラー: {e}")