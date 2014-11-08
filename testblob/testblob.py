__author__ = 'George'
from myro import *
init("COM3")

fn = "14.jpg"
fn2 = "14bblob.jpg"

pic = takePicture()
savePicture(pic, fn)

#configureBlob(y_low = 0, y_high = 190, u_low = 48, u_high = 248, v_low = 145, v_high = 255) #pink YUV
configureBlob(y_low = 200, y_high = 255, u_low = 100, u_high = 150, v_low = 100, v_high = 150)


blobpic = takePicture("blob")
savePicture(blobpic, fn2)
print getBlob()


