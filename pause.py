import keyboard
import subprocess
import time
import threading

# Global variables to control pause state and store the process
_paused = False
_process = None
_pause_event = threading.Event()
_resume_event = threading.Event()


def stop_microphone_process():
    """Stop the microphone process."""
    global _process
    if _process:
        _process.terminate()  # Terminate the microphone process
        _process = None

def toggle_pause():
    """Toggle the pause state when the space bar is pressed."""
    global _paused
    _paused = not _paused
    if _paused:
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(1)
        print("Bot paused.")
        stop_microphone_process()  # Stop the microphone process
        _pause_event.set()  # Signal the pause event
    else:
        print("Resuming...")
        print("Bot resumed.")
        print("") # Restart the microphone process
        _pause_event.clear()  # Clear the pause event
        _resume_event.set()  # Signal the resume event

def monitor_space_bar():
    """Monitor the space bar to toggle the pause state."""
    keyboard.add_hotkey('space', toggle_pause)
    keyboard.wait()  # This will keep the thread alive to listen for space bar presses

def start_pause_monitor():
    """Start monitoring for the space bar in a separate thread."""
    pause_thread = threading.Thread(target=monitor_space_bar, daemon=True)
    pause_thread.start()

def is_paused():
    """Return the current pause state."""
    return _paused

if __name__ == "__main__":
    start_pause_monitor()
