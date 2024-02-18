import ctypes
import time
import sys  # Import the sys module
from pynput import keyboard

# Function to turn off the screen
def screen_off():
    ctypes.windll.user32.SendMessageW(65535,   274,   61808,   2)
    print('Screen is turned off')

# Function to turn on the screen
def screen_on():
    ctypes.windll.user32.SendMessageW(65535,   274,   61808, -1)
    print('Screen is turned on')

# Turn off the screen immediately
screen_off()

# Function to be called when a key is pressed
def on_press(key):
    # Turn on the screen when any key is pressed
    screen_on()
    # Stop the listener
    listener.stop()  # Add this line to stop the listener
    # Terminate the script
    sys.exit()  # Add this line to terminate the script
    return False

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
