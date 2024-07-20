# Import necessary libraries
import json
import random
import speech_recognition as sr
from functions.speak import speak
from functions.response import get_response  # Import the function to get AI responses
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Load error messages from the JSON file
with open('data/error.json', 'r') as file:
    error_data = json.load(file)
    speech_recognition_errors = error_data["errors"]["speech_recognition"]
    service_errors = error_data["errors"]["service_error"]
    unknown_command_errors = error_data["errors"]["unknown_command"]

# Define the handle_error function to print error messages
def handle_error(error_message):
    """Handle errors and print the error message."""
    speak(error_message)

# Function to take command via microphone and process it
def take_command(mode):
    """Continuously listen for speech and convert it to text."""
    if mode == 'paused':
        return None  # Return None immediately if in paused mode

    r = sr.Recognizer()
    text = None
    
    if mode == 'command':
        print(Fore.YELLOW + "Listening for command...")
    elif mode == 'chat':
        print(Fore.YELLOW + "Let's have a talk...")

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(Fore.GREEN + ">>>", text)
            if mode == 'chat':
                response = get_response(text)
                print(Fore.BLUE + "AI Response:", response)
        except sr.UnknownValueError:
            handle_error(random.choice(speech_recognition_errors))
        except sr.RequestError:
            handle_error(random.choice(service_errors))
    
    return text.lower() if text else None