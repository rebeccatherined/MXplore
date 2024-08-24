import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(
    api_key=API_KEY
)

model=genai.GenerativeModel('gemini-1.5-flash')
chat=model.start_chat(history=[])
instruction="Suggest to tourists the different heritage sites, tourist spots , restaurants,shopping hubs, hotels to stay in and other stuff that tourists would like to see only in Madurai and the respond after asking and analysing their age, purpose of visit , food preferances, timings, reservations to make it personalised to this purpose"
print("Welcome to MXplore -Your tour Guide to Madrai!")
while(True):
    question = input("You: ")
    
    if(question.strip() == ''):
        break
    
    response = chat.send_message(instruction + question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')
    instruction = ''