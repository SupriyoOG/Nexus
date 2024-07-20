import os
import time
import click
import json
import random
from colorama import Fore, init
import sys

# Importing functions and modules from the functions directory
from functions import response
from functions.command_mode import execute_command
from functions.speak import speak
from functions.listen import take_command
from functions.password import verify_password, change_password
from functions.intro import intro_sequence
from functions.deletecache import delete_cache
from functions.forgot_password import main as reset_password
from functions.pause import start_pause_monitor, is_paused  # Import pause functions

# Initialize colorama
init(autoreset=True)
click.clear()

# Load greetings from the JSON file
with open('data/greetings.json', 'r') as file:
    data = json.load(file)
    greetings = data["greetings"]
    starting_messages = data["Starting"]
    started_messages = data["started"]

# Function to prompt for password reset
def prompt_reset_password():
    print(Fore.RED + "Too many incorrect attempts. Resetting your password...")
    reset_password()

# Function to ask user whether to delete cache files before exiting
def ask_delete_cache():
    """Ask the user whether to delete cache files before exiting."""
    response = input(Fore.YELLOW + "Do you want to delete cache files before exiting? (yes/no): ").strip().lower()
    return response == 'yes'

# Function to restart the script
def reboot_nexus():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Function to switch between chat and command modes
def switch_mode(input_text, current_mode):
    if input_text.strip().lower() == "switch to command mode":
        new_mode = 'command'
        speak("Switched to command mode.")
        print(Fore.GREEN + "Switched to command mode.")
    elif input_text.strip().lower() == "switch to chat mode":
        new_mode = 'chat'
        speak("Switched to chat mode.")
        print(Fore.GREEN + "Switched to chat mode.")
    else:
        new_mode = current_mode
    return new_mode

# Main function to handle user commands
@click.command()
def main():
    print(Fore.YELLOW + random.choice(starting_messages))  # Print random starting message
    time.sleep(1)
    print(Fore.GREEN + random.choice(started_messages))
    time.sleep(1)

    # Check password before proceeding
    def check_password():
        for _ in range(3):  # Allow up to 3 attempts
            input_password = input("Enter password: ")
            if verify_password(input_password):
                return True
            else:
                print(Fore.RED + "Incorrect password. Try again.")
        return False

    if not check_password():
        prompt_reset_password()

    # Run intro sequence
    intro_sequence()

    # Default mode
    mode = 'command'

    # Initial greeting
    introduction = random.choice(greetings)
    speak(introduction)

    # Start monitoring for pause/resume
    start_pause_monitor()

    # Function to process user input based on mode
    def process_input(input_text):
        nonlocal mode
        if mode == 'chat':
            if 'switch to command mode' in input_text.lower():
                mode = switch_mode("switch to command mode", mode)
            else:
                ai_response = response.get_response(input_text)
                # print(ai_response)
                speak(ai_response)
        elif mode == 'command':
            if 'switch to chat mode' in input_text.lower():
                mode = switch_mode("switch to chat mode", mode)
            else:
                if any(keyword in input_text.lower() for keyword in ['bye', 'exit', 'quit', 'shutdown', 'shut down']):
                    speak("Goodbye!")
                    print(Fore.RED + "Goodbye!")
                    if ask_delete_cache():
                        delete_cache()
                    sys.exit(0)
                elif 'change password' in input_text.lower():
                    change_password()
                elif 'reboot' in input_text.lower():
                    speak("Restarting Nexus...")
                    print(Fore.YELLOW + "Restarting Nexus...")
                    time.sleep(2)
                    reboot_nexus()
                else:
                    command_response = execute_command(input_text, mode)
                    if command_response and 'Warning' not in command_response:
                        speak(command_response)
                    else:
                        print(command_response)

    # Listen for commands
    while True:
        if is_paused():
            time.sleep(0.1)  # Small delay to avoid busy-waiting
            continue  # Skip the listening loop if paused

        user_input = take_command(mode)
        if user_input:
            process_input(user_input)

if __name__ == "__main__":
    main()
