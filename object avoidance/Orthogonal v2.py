__author__ = 'George'

from myro import *
from random import randint
init("COM3")

#Anger
anger = ["damit", "fucking wall o m g", "I dont like this wall", "wall you bastard", "stupid wall g t f o", "this wall dough", "why you block me"]

timewait = 0.5
spd = 0.6
tint = 0.45
rightturn = 0.3
leftturn = 0.63
tracker = 0


def approachWall():
    while (getObstacle("middle")==0):
        forward(spd)
    stop()
    print (getObstacle("middle"))
    forward(0.35, 0.4)
    speak("Holy shit a wall", 0)

def followWall():
    global tracker
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
        tracker += 1
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
followWall()
turnCorner()
followWall()
turnCorner2()
tracker /= 2
tracker += 2
forward(spd, tint*tracker)
turnRight(1, 0.7)

#hand motion sto[p
while (getObstacle("middle")==0):
    move(1, 0)
stop()


