from myro import *

def activated(self):
    #insert sensor checking for objects
    speak("Security is now activated, to deactivate, cover the left light sensor.")

    #If all sensors are covered, go to password entry.
    while (1):
        wait(0.5)
        print getLight()
        if getLight ("left") > self.__leftS:
            if not self.__lockedOut:
                checkPassword()
            else:
                speak("You have been locked out.")

def deactivated(self):
    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left light sensor.", 0)
    speak("To change password, cover the center light sensor.", 0)

    while(1):
        wait(0.5)
        if getLight("left") > self.__leftS:
            activated()

        if getLight("center") > self.__centerS:
            checkPassword()
            self.__password = setPassword()


def main ():
    init("COM3")
    password = setPassword()

    #Puts the robot in deactivated mode, pending activation.
    deactivated(password)

main()
