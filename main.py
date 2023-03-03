import time
import pydirectinput
import dxcam

cam = dxcam.create()

class Circle:
    white = (255,255,255)
    blue = (125, 205, 255)
    x = 1280
    y = 1335
    bottomy = 1385

class UkraneFlag:
    blue = (52, 201, 255)
    yellow = (255, 206, 28)
    x = 1075
    y = 1179

def checkUkrane():
    frame = cam.grab()
    while frame is None:
        frame = cam.grab()

    bluePixels = set()
    for i in range(410):
        color = tuple(frame[UkraneFlag.y, UkraneFlag.x + i])
        if color == UkraneFlag.blue:
            bluePixels.add(i)

    yellowOnBlue=False
    while not yellowOnBlue:
        frame = cam.grab()
        while frame is None:
            frame = cam.grab()
        for i in bluePixels:
            if tuple(frame[UkraneFlag.y, UkraneFlag.x + i]) == UkraneFlag.yellow:
                pydirectinput.click(Circle.x, Circle.bottomy)
                yellowOnBlue = True
                print(F"Detected: {UkraneFlag.x + i}")
                break

def checkfishon():
    frame = cam.grab()
    while frame is None:
        frame = cam.grab()

    color = tuple(frame[Circle.y, Circle.x])
    return color == Circle.white or color == Circle.blue

fishCount = 0
time.sleep(3)
while True:
    pydirectinput.click(1280, 720)

    while not checkfishon():
        time.sleep(0.1)

    while checkfishon():
        checkUkrane()
        time.sleep(0.1)

    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)

    fishCount += 1
    print(f"Caught Fish: {fishCount}\n")