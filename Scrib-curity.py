from myro import*

#This variable keeps track of the number of incorrect password attempts
#At a certain amount, it will lock out the robot for a set number of minutes.
wrongTries = 0

def get_password():
    #read left, middle, right sensors
    speak ("Enter your six digit password", 0)
    password = [6]
    count = 0
    while (count<6):
        if getLight ("left") > 4000:
            password[count] = "left"
            count++
            beep(.5, 800)

        elif getLight("center") > 4000:
            password[count] = "center"
            count++
            beep(.5, 800)

        elif getLight("right") > 4000:
            password[count] = "right"
            count++
            beep(.5, 800)

    speak("your password has been set", 0)
    return password

def check_password (password):
    count = 0
    while (count<6):
        if getLight ("left") > 4000:
            if password[count] == "left":
                count++
                beep(.5, 800)
            else:
                wrongPassword()

        elif getLight("center") > 4000:
            if password[count] == "center:":
                count++
                beep(.5, 800)
            else
                wrongPassword()

        elif getLight("right") > 4000:
            if password[count] == "right":
                count++
                beep(.5, 800)
            else:
                wrongPassword()

def wrongPassword():
    global wrongTries++
    speak("you have entered an incorrect password", 0)
    activated()

def check_activation():
    if getLight("left") > 4000:
        return True
    else:
        return False

def activated():
    #insert sensor checking for objects

    if removed:



def change_password():
    #Input password from user to de-activate security system
    if getLight("middle") > 4000:
        return True
    else:
        return False

def deactivate():


def main ():
    password = []
    password = get_password()

    while(1):
        if check_activation():
            activated()

        if change_password():
            password = get_password()