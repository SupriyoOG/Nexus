import platform
import subprocess
import os
import shutil
import sys
import click
from colorama import Fore
from functions.password import change_password
from functions.speak import speak

def list_files():
    """List files in the current directory."""
    files = os.listdir('.')
    print(Fore.GREEN + "Files in current directory:")
    for file in files:
        print(file)

def execute_command(command, mode='command'):
    """Execute system commands based on user input."""
    try:
        if 'open notepad' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            subprocess.Popen('notepad.exe')
            print(Fore.GREEN + "Opening Notepad...")
        elif 'open calculator' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            subprocess.Popen('calc.exe')
            print(Fore.GREEN + "Opening Calculator...")
        elif 'open code' in command or 'open visual studio code' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            subprocess.Popen('Code.exe')
            print(Fore.GREEN + "Opening Visual Studio Code...")
        elif 'shutdown' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            print(Fore.RED + "Shutting down the program...")
            exit()
        elif 'open file explorer' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            subprocess.Popen('explorer.exe')
            print(Fore.GREEN + "Opening File Explorer...")
        elif 'list files' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            list_files()
        elif 'create folder' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            folder_name = command.split('create folder ')[-1]
            os.makedirs(folder_name, exist_ok=True)
            print(Fore.GREEN + f"Folder '{folder_name}' created successfully.")
        elif 'delete folder' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            folder_name = command.split('delete folder ')[-1]
            shutil.rmtree(folder_name, ignore_errors=True)
            print(Fore.GREEN + f"Folder '{folder_name}' deleted successfully.")
        elif 'rename file' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            params = command.split('rename file ')[-1].split(' to ')
            old_name = params[0]
            new_name = params[1]
            os.rename(old_name, new_name)
            print(Fore.GREEN + f"File '{old_name}' renamed to '{new_name}' successfully.")
        elif 'start game' in command:  # Adjust the command as needed
            game_process = subprocess.Popen([sys.executable, 'game/game.py'])
            print(Fore.GREEN + "Launching game...")
            game_process.wait()  # Wait until the game process finishes
            speak(Fore.GREEN + "Game closed. Resuming...")
            print(Fore.GREEN + "Game closed. Resuming...")
        elif 'clear terminal' in command:
            if mode == 'chat':
                return "Warning: This command requires switching to command mode."
            click.clear()
        elif 'change password' in command:
            change_password()
        else:
            return "Command not recognized. Please try again."
    except Exception as e:
        print(Fore.RED + f"Failed to execute command: {e}")

    return None
