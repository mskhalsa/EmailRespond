import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def mock_openai_response(subject: str, body: str) -> str:
    """Real LLM call with OpenAI SDK v1.x, response must be quick."""
    prompt = (
        f"Subject: {subject}\n\n"
        f"{body}\n\n"
        f"Write a short, professional email reply."
    )

    try:
        start = time.time()
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100,
            timeout=0.8
        )
        duration = time.time() - start
        print(f"LLM responded in {duration:.2f}s")
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"OpenAI error: {e}")
        return "Thank you for your message. I'll get back to you soon."
