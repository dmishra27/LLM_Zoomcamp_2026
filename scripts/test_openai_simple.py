from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Hello"
    )
    print(response.output_text)
except Exception as e:
    print(type(e).__name__)
    print(e)