import playsound
from colorama import Fore
from functions.speak import speak

# Function to play mode change sound
def play_mode_change_sound():
    playsound('data/changing.wav')

# Function to switch between modes
def switch_mode(input_text, current_mode):
    """Switch between chat and command mode based on user input."""
    new_mode = current_mode
    if input_text.strip().lower() == "switch to command mode":
        new_mode = 'command'
        speak("Switched to command mode.")
        print(Fore.GREEN + "Switched to command mode.")
    elif input_text.strip().lower() == "switch to chat mode":
        new_mode = 'chat'
        speak("Switched to chat mode.")
        print(Fore.GREEN + "Switched to chat mode.")
    return new_mode
