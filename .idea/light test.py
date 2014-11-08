from myro import *
init("COM3")

while(True):
    if getLight("left") < 60000:
        beep(1, 800)
    elif getLight("center") < 60000:
        beep(1, 1000)
    elif getLight("right") < 60000:
        beep(1, 1200)
    wait(1)