from myro import *
import math

def isBlack(pixel):
    rgb = pixel.getRGB()[0]
    if rgb==255:
        return False
    elif rgb==0:
        return True
    else:
        return True

def countBlack(pic, xlow, xhigh, ylow, yhigh):
    counter = 0;
    for x in range(xlow, xhigh):
        for y in range(ylow, yhigh):
            if (isBlack(getPixel(pic, x,y)) == True):
                counter+=1
    return counter;

def xBounds(pic):
    ## find x-bounds
    for xlow in range (0, 1280):
        if (isBlack(getPixel(pic,xlow,400)) == False):
            for xhigh in range (xlow, 1280):
                if (isBlack(getPixel(pic,xhigh,400)) == True):
                    return [xlow, xhigh, xhigh-xlow]
    return "YOU FUCKED UP"

def yBounds(pic):
    ## find y-bounds
    for ylow in range (0, 800):
        if (isBlack(getPixel(pic,640,ylow)) == False):
            for yhigh in range (ylow, 800):
                if (isBlack(getPixel(pic,640,yhigh)) == True):
                    return [ylow, yhigh, yhigh-ylow]


init("COM6")
configureBlob(200, 255, 100, 150, 100, 150)
frametol = 10
thieftol = 50

## Information about the screen itself
picture = takePicture("blob")
savePicture(picture, "first.jpg")
[xlow, xhigh, xdiff] = xBounds(picture)
[ylow, yhigh, ydiff] = yBounds(picture)
print("x-lower: " + str(xlow) + "; x-upper: " + str(xhigh))
print("y-lower: " + str(ylow) + "; y-upper: " + str(yhigh))
area = xdiff * ydiff
print("iteration space: " + str(area))

## Place your objects
speak("place your objects")
for i in range (0,5):
    speak("do it now")
    wait(1)
## Information about the initial object setup
picture = takePicture("blob")
black0 = countBlack(picture, xlow+frametol,xhigh-frametol, ylow+frametol, yhigh-frametol)


## Loop
for i in range (0,10):
    picture = takePicture("blob")
    black1 = countBlack(picture, xlow+frametol,xhigh-frametol, ylow+frametol, yhigh-frametol)
    print("i=" + str(i) + "; black0=" + str(black0) + "; black1=" + str(black1))
    if (black0 - black1 > thieftol):
        speak("you took something")
    if (black1 - black0 > thieftol):
        speak("you put something back")
    black0 = black1
