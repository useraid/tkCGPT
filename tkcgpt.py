import requests
import tkinter as tk
from tkinter import simpledialog, messagebox
from dotenv import load_dotenv
import os
import datetime

def secret():
    load_dotenv()

secret()

application_window = tk.Tk()
userInput = simpledialog.askstring("Input", "How can I help you today?",
                               parent=application_window)

# OAI Request
openai_api_ep = "https://api.openai.com/v1/completions"
api_key = os.getenv('api_key')

postHeader = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

postData = {
    "model": "text-davinci-003",
    "prompt": f"{userInput}",
    "max_tokens": 200,
    "temperature": 0.5
}

response = requests.post(openai_api_ep, headers=postHeader, json=postData)

# Output
if response.status_code == 200:
    output = response.json()["choices"][0]["text"]
    if userInput is not None:
        messagebox.showinfo("Information",f"{output}")
    # Logging    
    timeStamp = "\n" + str(datetime.datetime.now())
    with open("tkcgpt.log", "a") as file:
        file.write(timeStamp)
        file.write(output)

else:
    print(f"Malformed/Invalid Response \nStatus Code: {str(response.status_code)}")
