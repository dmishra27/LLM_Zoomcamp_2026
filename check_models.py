from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

try:
    models = client.models.list()
    print("SUCCESS")
    print(f"Found {len(models.data)} models")
except Exception as e:
    print(type(e).__name__)
    print(e)