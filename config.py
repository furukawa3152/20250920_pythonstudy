import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

if not API_KEY:
    raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません。")