from myro import *
import time
#This variable keeps track of the number of incorrect password attempts
#At a certain amount, it will lock out the robot for a set number of minutes.
startTime = time.time()
errorTime = 0
wrongTries = 0
lockedOut = False




def checkActivation():
    if getIR("left") == 1:
        return True
    else:
        return False

def isChangePassword():
    #Input password from user to deactivate security system
    if getIR("right") == 1:
        return True
    else:
        return False


def getPassword():
    #read left, right sensors
    speak ("Enter your six digit password", 0)
    password = []

    while (len(password) < 6):
        if getIR("left") == 1:
            password.append("left")
            beep(.5, 800)


        elif getIR("right") == 1:
            password.append("right")
            beep(.5, 800)

    speak("your password has been set", 0)
    return password

def checkPassword (password, isChange):
    speak("Please enter your password.")
    for count in range (6):
        if getIR("left") == 1:
            if password[count] == "left":
                beep(.5, 800)
            else:
                wrongPassword()

        elif getIR("right") == 1:
            if password[count] == "right":
                beep(.5, 800)
            else:
                wrongPassword()
        beep(.5, 800)

    if (not isChange):
        speak("Password entered successfully. Security deactivated.")
    else:
        speak("Password changed successfully. Security remains deactivated.")

    deactivated()

def wrongPassword():
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
    activated()



def activated(password):
    #insert sensor checking for objects
    speak("Security is now activated, to deactivate, cover all both IR sensors.")

    #If all sensors are covered, go to password entry.
    while (1):
        if getIR("left") == 1 and getIR(right) == 1 and not lockedOut:
            checkPassword(password, False)


def deactivated(password):
    while(1):
        if checkActivation():            
            activated(password)

        if isChangePassword():
            checkPassword(password, True)
            password = getPassword()


def main ():
    init("COM3")
    password = getPassword()

    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left IR sensor.", 0)

    #Puts the robot in deactivated mode, pending activation.
    deactivated(password)

main()