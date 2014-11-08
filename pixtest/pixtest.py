from myro import *

def getbw(pixel):
    rgb = pixel.getRGB()
    if rgb[0]>=200 and rgb[1]>=200 and rgb[2]>=200:
        return " "
    elif rgb[0]<=55 and rgb[1]<=55 and rgb[2]<=50:
        return "$"
    else:
        return "-1"

bitmap = []
pic = makePicture("bit-test.jpg")
print pic.width
for h in range(0, pic.height):
    out = []
    for w in range(0, pic.width):
        out.append(getbw(getPixel(pic, w, h)))
    bitmap.append(out)

for i in range(len(bitmap)):
    print bitmap[i]

