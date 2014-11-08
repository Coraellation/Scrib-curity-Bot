from myro import *
init("COM3")

f = 0.1
while getObstacle("middle") == 0:
    beep(f, 2903, 1975.53)
    beep(f, 2093, 1864.66)
    beep(f, 2093, 1760)
    beep(f, 2093, 1661.22)