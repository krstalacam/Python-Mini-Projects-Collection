import datetime
import pyautogui
import time
import os

SHUTDOWN_CMD = "shutdown /s /t 60"
SHUTDOWNCANCEL_CMD = "shutdown /a"


def box2():
    while True:
        if pyautogui.position() != (positionmouse.x, positionmouse.y):
            os.system(SHUTDOWNCANCEL_CMD)
            break


while True:
    positionmouse = pyautogui.position()
    time.sleep(1800)
    current_time = datetime.datetime.now().time()
    if current_time <= datetime.time(8):
        if pyautogui.position() == (positionmouse.x, positionmouse.y):
            os.system(SHUTDOWN_CMD)
            box2()
