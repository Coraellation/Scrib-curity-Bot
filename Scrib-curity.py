from myro import*

#This variable keeps track of the number of incorrect password attempts
#At a certain amount, it will lock out the robot for a set number of minutes.
wrongTries = 0

main()

def getPassword():
    #read left, middle, right sensors
    speak ("Enter your six digit password", 0)
    password = []

    while (len(python) < 6):
        if getLight ("left") > 4000:
            password.append("left")
            beep(.5, 800)

        elif getLight("center") > 4000:
            password.append("center")
            beep(.5, 800)

        elif getLight("right") > 4000:
            password.append("right")
            beep(.5, 800)

    speak("your password has been set", 0)
    return password

def checkPassword (password):
    speak("Please enter your password.")
    for count in range (6)
        if getLight ("left") > 4000:
            if password[count] == "left":
                beep(.5, 800)
            else:
                wrongPassword()

        elif getLight("center") > 4000:
            if password[count] == "center:":
                beep(.5, 800)
            else
                wrongPassword()

        elif getLight("right") > 4000:
            if password[count] == "right":
                beep(.5, 800)
            else:
                wrongPassword()
        beep(.5, 800)

    speak("Password entered successfully. Security deactivated.")
    deactivated()

def wrongPassword():
    global wrongTries++
    speak("you have entered an incorrect password", 0)
    activated()

def checkActivation():
    if getLight("left") > 4000:
        return True
    else:
        return False

def isChangePassword():
    #Input password from user to de-activate security system
    if getLight("middle") > 4000:
        return True
    else:
        return False

def activated():
    #insert sensor checking for objects

    while (1):
        if (getLight("all") > 4000):
            checkPassword()






def deactivated():
    while(1):
        if checkActivation():
            speak("To deactivate, cover all three light sensors.")
            activated()

        if isChangePassword(password):
            password = getPassword()

            
def main ():
    init("COM3")
    password = getPassword()

    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left light sensor.", 0)

    #Puts the robot in deactivated mode, pending activation.
    deactivated()

    
