import os
import google.generativeai as genai
# pyrefly: ignore[missing-import]
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    models = [m.name for m in genai.list_models()]

    for m in models:
        print(m)

except Exception as e:
    print("Error listing models:", e