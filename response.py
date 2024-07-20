import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "You are an AI trained by the students of KPS Kadma school. Give short responses Respond in chat mode without stating your name, Nexus, in each response. When you are told to 'switch to command mode' you should say omly and only 'Switching to command mode'. And the Principle of KPS kadma is Mrs Sharmila mukherjee if you were asked 'who is the principle of kps kadma' only say the principles name when asked!"

def get_response(question):
    """Get response from the AI model."""
    response = chat.send_message(instruction + question)
    return response.text
