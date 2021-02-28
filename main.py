import pyautogui

pyautogui.sleep(2)


def press(key, dur, times):
    for i in range(0, times):
        print(key)
        pyautogui.keyDown(key)
        pyautogui.sleep(dur)
        pyautogui.keyUp(key)
        pyautogui.sleep(longkeypress)


while True:

    keypress = 0.1
    longkeypress = 0.25

    press('up', 0.01, 1)
    pyautogui.sleep(5)

    press(key='down', dur=keypress, times=7)
    pyautogui.sleep(2)
    press(key='right', dur=keypress, times=8)
    press(key='up', dur=keypress, times=2)
    pyautogui.sleep(2)

    press(key='left', dur=keypress, times=2)
    for x in range(0, 6):
        press(key='9', dur=keypress, times=1)
        pyautogui.sleep(12)
        press(key='z', dur=keypress, times=3)
        pyautogui.sleep(15)
        for i in range(0, 2):
            press(key='x', dur=keypress, times=1)
            press(key='z', dur=keypress, times=1)
            pyautogui.sleep(5)

    press(key='right', dur=keypress, times=1)
    press(key='down', dur=keypress, times=1)
    pyautogui.sleep(3)


    press(key='down', dur=keypress, times=1)
    press(key='left', dur=keypress, times=9)
    pyautogui.sleep(3)

    press(key='up', dur=keypress, times=1)
    pyautogui.sleep(3)
    press(key='up', dur=keypress, times=6)
    press(key='z', dur=keypress, times=4)
    pyautogui.sleep(5)
    for i in range(0, 2):
        press(key='z', dur=keypress, times=1)
    pyautogui.sleep(3)
    press(key='z', dur=keypress, times=1)
