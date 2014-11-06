from myro import *
import time
#This variable keeps track of the number of incorrect password attempts
#At a certain amount, it will lock out the robot for a set number of minutes.
startTime = time.time()
errorTime = 0
wrongTries = 0
lockedOut = False

#GLOBAL light variables (for sensitivity)
leftS = 65000;
centerS = 65300;
rightS = 64600;



def checkActivation():
    global leftS
    wait (0.5)
    if getLight("left") >leftS:
        return True
    else:
        return False

def isChangePassword():
    global rightS
    #Input password from user to deactivate security system
    wait(0.5)
    if getLight("center") > 65380:
        return True
    else:
        return False


def getPassword():
    global leftS
    global centerS
    global rightS
    #read left, middle, right sensors
    speak ("Enter your six digit password", 0)
    password = []

    while len(password) < 6:
        wait(0.5)
        if getLight("left") > leftS:
            password.append("left")
            print getLight("left")
            beep(.5, 800)

        elif getLight("center") > centerS:
            password.append("center")
            print getLight("center")
            beep(.5, 1000)

        elif getLight("right") > rightS:
            password.append("right")
            print getLight("right")
            beep(.5, 1200)
    print password

    speak("your password has been set", 0)
    return password

def checkPassword (password, isChange):
    global wrongTries
    global leftS
    global centerS
    global rightS

    speak("Please enter your password.")
    for count in range(6):
        while (1):
            wait(0.5)
            if getLight("left") > leftS:
                if password[count] == "left":
                    beep(.5, 800)
                    break
                else:
                    wrongPassword(password)

            elif getLight("center") > centerS:
                if password[count] == "center":
                    beep(.5, 1000)
                    break
                else:
                    wrongPassword(password)

            elif getLight("right") > rightS:
                if password[count] == "right":
                    beep(.5, 1200)
                    break
                else:
                    wrongPassword(password)
    wrongTries = 0
    if (not isChange):
        speak("Password entered successfully. Security deactivated.")
    else:
        speak("Password changed successfully. Security remains deactivated.")

    deactivated(password)

def wrongPassword(password):
    global wrongTries
    global errorTime
    global lockedOut

    #Sets time of first error.
    if wrongTries == 0:
        errorTime = time.time()

    wrongTries +=1

    if wrongTries == 3 and (time.time() - errorTime) < 600:
        speak("You have entered an incorrect password three times. The robot will be locked out for 10 minutes.")
        lockedOut = True
        wrongTries = 0

    speak("You have entered an incorrect password", 0)
    activated(password)



def activated(password):
    global leftS
    #insert sensor checking for objects
    speak("Security is now activated, to deactivate, cover the left light sensor.")

    #If all sensors are covered, go to password entry.
    while (1):
        wait(0.5)
        print getLight()
        if getLight ("left") > leftS and not lockedOut:
            checkPassword(password, False)


def deactivated(password):
    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left light sensor.", 0)
    speak("To change password, cover the center light sensor.", 0)

    while(1):
        wait(0.5)
        if checkActivation():            
            activated(password)

        if isChangePassword():
            checkPassword(password, True)
            password = getPassword()


def main ():
    init("COM3")
    password = getPassword()



    #Puts the robot in deactivated mode, pending activation.
    deactivated(password)

main()