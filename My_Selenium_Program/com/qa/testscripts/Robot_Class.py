import pyautogui
import time

# Give you 5 seconds to move your cursor to the desired window (e.g., Notepad)
print("Starting in 5 seconds...")
time.sleep(5)

# Move mouse to coordinates (x=400, y=300)
pyautogui.moveTo(400, 300, duration=1)
pyautogui.click()  # Perform mouse click

# Type text
pyautogui.write("Hello from Python Robot Class equivalent!", interval=0.1)

# Press Enter key
pyautogui.press('enter')

# Type more
pyautogui.write("This simulates mouse and keyboard events.", interval=0.1)
pyautogui.press('enter')

# Hotkey example: Select all and delete
pyautogui.hotkey('ctrl', 'a')   # Ctrl + A to select all
time.sleep(1)
pyautogui.press('backspace')    # Delete selected text
