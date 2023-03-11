import pyautogui
import time
def end(n):
        pyautogui.moveTo(x=-717, y=103,duration=1)
        pyautogui.click()
        pyautogui.moveTo(x=-547, y=237,duration=1)
        pyautogui.click()
        pyautogui.moveTo(x=-448, y=472,duration=1)
        pyautogui.click()

def fix(n):
    pyautogui.moveTo(x=-182, y=479,duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=-809, y=192,duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=-222, y=408,duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=-448, y=399,duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=-62, y=47,duration=1)
    pyautogui.click()

def eat(n):
    pyautogui.moveTo(x=-689, y=473,duration=1)
    pyautogui.click()

n=int(input())
a=0
for i in range(0,n):
    time.sleep(200)
    eat(n)
    a+=1
    if a==70:
        fix(n)
        a=0

end(n)