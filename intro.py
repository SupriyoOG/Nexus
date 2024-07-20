# intro.py
import os
import time
from playsound import playsound  # Ensure you have playsound module installed
from colorama import Fore

from colorama import Fore

def display_ascii_art():
    """Display ASCII art of 'NEXUS'."""
    nexus_art = Fore.GREEN + """
    
    ███╗   ██╗███████╗ ██╗ ██╗ ██╗   ██╗███████╗
    ████╗  ██║██╔════╝ ██║ ██╔╝██║   ██║██╔════╝
    ██╔██╗ ██║█████╗    ████╔╝ ██║   ██║███████╗
    ██║╚██╗██║██╔══╝   ██╔ ██╗ ██║   ██║╚════██║
    ██║ ╚████║███████╗m██║ ██╗╚██████╔╝███████║
    ╚═╝  ╚═══╝╚══════╝╚═╝    ╚═╝ ╚═════╝ ╚══════╝
                                           
                                           

    """
    print(nexus_art)


def play_intro_music():
    """Play intro music."""
    try:
        playsound(f'data/start.wav')
    except Exception as e:
        print("Error playing music:")

def intro_sequence():
    """Run the intro sequence with ASCII art and music."""
    display_ascii_art()
    play_intro_music()
    time.sleep(1)  # Add delay for dramatic effect
