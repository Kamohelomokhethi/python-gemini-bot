import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

while True:
    query = input("you: ")

    if query.strip() == "":
        break

    response = chat.send_message(query)
    print("\n")
    print(f"bot: {response.text} \n")
