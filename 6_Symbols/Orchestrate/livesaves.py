import pyautogui
import time

# Set the interval for saving the transcription
interval = 5  # seconds

while True:
    # Copy the transcription text
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Open Notepad and paste the text
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('notepad\n', interval=0.1)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.typewrite('transcription.txt\n', interval=0.1)
    time.sleep(interval)