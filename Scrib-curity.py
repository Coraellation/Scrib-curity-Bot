from myro import *
import Security

security = Security.Security()


def activated(self):
    global security
    #insert sensor checking for objects
    speak("Security is now activated, to deactivate, cover the left light sensor.")

    #If all sensors are covered, go to password entry.
    while (1):
        wait(0.5)
        print getLight()
        if getLight ("left") > security.getLeftS():
            if not self.__lockedOut:
                if security.checkPassword():
                    deactivated()
                else:
                    security.wrongPassword()
            else:
                speak("You have been locked out.")

        security.checkLockedOut()


def deactivated(self):
    global security

    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left light sensor.", 0)
    speak("To change password, cover the center light sensor.", 0)

    while(1):
        wait(0.5)
        if getLight("left") > security.getLeftS():
            activated()

        if getLight("center") > security.getCenterS():
            security.checkPassword()
            self.__password = security.setPassword()


def main():
    global security
    init("COM3")
    security.setPassword()
    deactivated()

main()
