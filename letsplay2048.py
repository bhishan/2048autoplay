import pyautogui
import time
pyautogui.click(721,41);pyautogui.typewrite('https://gabrielecirulli.github.io/2048/',interval=0.10);pyautogui.press('enter')
time.sleep(10)
for i in range(400):
    pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('left')
    time.sleep(0.2)
    pyautogui.press('up')
    time.sleep(0.2)
