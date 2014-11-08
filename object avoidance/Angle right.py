__author__ = 'George'

from myro import *
from random import randint
init("COM3")

timewait = 0.5
spd = 0.8
tint = 0.5
rightturn = 0.26
leftturn = 0.60


def approachWall():
    while (getObstacle("middle")==0):
        forward(spd)
    stop()
    print (getObstacle("middle"))
    speak("Holy shit a wall", 0)

def followWall():
    while (getObstacle("middle") != 0):

        timer = 0
        while (getObstacle("middle")):
            timer += 1
            move(0, -1)
        stop()
        print(timer)
        if (timer>3):
            turnRight(1, rightturn)
        else:
            turnRight(1, rightturn +0.18)
        wait(timewait)
        forward(spd, tint)
        wait(timewait)
        turnLeft(1, leftturn)
        wait(timewait)
        print getObstacle("middle")
        wait(timewait)
    speak ("I'm fat", 0)

def turnCorner():
    turnRight(1, 0.78)

    while(getObstacle("middle") == 0):
        move(1, 0.75)
    stop()
    speak("next wall", 0)
    turnLeft(1, 0.25)

def turnCorner2():
    turnRight(1, 0.76)

    forward(1, 0.5)
    wait(timewait)
    turnLeft(1, leftturn)


approachWall()
turnLeft(1, 0.2)
wait(timewait)
followWall()
turnCorner()
followWall()
turnRight(1, 1.1)

#hand motion sto[p
while (getObstacle("middle")==0):
    move(1, 0)
stop()


