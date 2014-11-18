## IMPORTANT IMPORTS

from myro import *
import math
import time

## GLOBAL VARIABLES
xlow = 0
xhigh = 0
ylow = 0
yhigh = 0
black0 = 0
black1 = 0
frametol = 10
thieftol = 100
i=0
f = 0.1
alarmtime = 50

## placeObjects is the function that prompts the user to put their objects in front of the screen.
## this function is called only once.
def placeObjects():
    ## Place your objects
    speak("Place your objects now.")
    words = ["five seconds", "four seconds", "three seconds", "two seconds", "one second"]
    for i in range (0,5):
        speak(words[i] + " left.")
        wait(1)
    picture = takePicture("blob")
    global black0
    black0 = countBlack(picture)

## setBounds is the function that defines xlow, xhigh, ylow, and yhigh, values that are used to count black pixels later on. 
## this function is called only once. 
def setBounds():
    configureBlob(200, 255, 100, 150, 100, 150)
    picture = takePicture("blob")
    savePicture(picture, "first.jpg")
    global xlow
    global xhigh
    global ylow
    global yhigh
    [xlow, xhigh, xdiff] = xBounds(picture)
    [ylow, yhigh, ydiff] = yBounds(picture)
    print("x-lower: " + str(xlow) + "; x-upper: " + str(xhigh))
    print("y-lower: " + str(ylow) + "; y-upper: " + str(yhigh))
    area = xdiff * ydiff
    print("iteration space: " + str(area))

## this function returns true if a given pixel is black.
## this function is called multiple times by countBlack.
def isBlack(pixel):
    rgb = pixel.getRGB()[0]
    if rgb==255:
        return False
    elif rgb==0:
        return True
    else:
        return True

## this function returns the number of black pixels in a given picture.
## this function is called in the alarmIterate() function.
def countBlack(pic):
    counter = 0;
    for x in range(xlow+frametol, xhigh-frametol):
        for y in range(ylow+frametol, yhigh-frametol):
            if (isBlack(getPixel(pic, x,y)) == True):
                counter+=1
    return counter;

## this function is used to find xlow and xhigh. It is called by setBounds() once.
def xBounds(pic):
    ## find x-bounds
    for x_lower in range (0, 1280):
        if (isBlack(getPixel(pic,x_lower,400)) == False):
            for x_upper in range (x_lower, 1280):
                if (isBlack(getPixel(pic,x_upper,400)) == True):
                    return [x_lower, x_upper, x_upper-x_lower]

## this function is used to find ylow and yhigh. It is called by setBounds() once.
def yBounds(pic):
    ## find y-bounds
    for y_lower in range (0, 800):
        if (isBlack(getPixel(pic,640,y_lower)) == False):
            for y_upper in range (y_lower, 800):
                if (isBlack(getPixel(pic,640,y_upper)) == True):
                    return [y_lower, y_upper, y_upper-y_lower]

## this function takes pictures, counts the black pixels, and sounds the alarm if an object is removed.
## this function is meant to be called in a while loop.
def alarmIterate():
    global i
    picture = takePicture("blob")
    global black0
    global black1
    black1 = countBlack(picture)
    print("i = " + str(i) + "; black0=" + str(black0) + "; black1=" + str(black1))
    if (black0 - black1 > thieftol):
        speak("You took something!")
        for w in range (0,4):
            alarmSound()
    #if (black1 - black0 > thieftol):
    #    speak("you put something back")
    black0 = black1-30
    i+=1

## this function just sounds an alarm lol. it is meant to be called in a for loop so it beeps a given number of times.
def alarmSound():
    beep(f, 2903, 1975.53)
    beep(f, 2093, 1864.66)
    beep(f, 2093, 1760)
    beep(f, 2093, 1661.22)

##  EVERYTHING STARTS HERE 
## these functions must be called.


