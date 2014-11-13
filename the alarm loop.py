from myro import *
import math
init("COM3")

def isBlack(pixel):
    rgb = pixel.getRGB()
    if rgb[0]==255:
        return False
    elif rgb[0]==0:
        return True
    else:
        return True

def countBlack(pic):
    blackcount = 0
    for h in range(0, pic.height):
        for w in range(0, pic.width):
            if isBlack(getPixel(pic, w, h)):
                blackcount += 1
    return blackcount
configureBlob(200, 255, 100, 150, 100, 150)
lastblack = 0
nowblack = 0

tolerance = 5000
while True:
    picture = takePicture("blob")
    lastblack = nowblack
    nowblack = countBlack(picture)

    print "last: ", lastblack
    print "now: ", nowblack
    if (lastblack - nowblack > tolerance):
        speak("thief")




