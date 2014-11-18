from myro import *
import Security

#The security system is a Global for now.
security = Security.Security()


def activated(self):
    '''This runs while the robot is activated.
    It checks to see if the user wants to deactivate the system.
    '''
    global security
    #insert sensor checking for objects
    speak("Security is now activated, to deactivate, cover the left light sensor.")

    #If the left sensor is covered, go to password entry.
    while (1):
        wait(0.5)
        print getLight()
        if getLight ("left") > security.getLeftS():
            #If it's not locked out, it allows for deactivation
            if not self.__lockedOut:
                if security.checkPassword():
                    deactivated()
                else:
                    security.wrongPassword()
            else:
                speak("You have been locked out.")

        security.checkLockedOut()


def deactivated(self):
    '''This runs while the robot is deactivated.
    Checks to see if the user wants to activate the system
    or change the password.
    '''
    global security

    speak("The robot is ready to be activated.", 0)
    speak("To activate, cover left light sensor.", 0)
    speak("To change password, cover the center light sensor.", 0)

    while(1):
        wait(0.5)
        #If the left sensor is covered, it activates
        if getLight("left") > security.getLeftS():
            activated()

        #If the center sensor is covered, you can change your password
        if getLight("center") > security.getCenterS():
            if security.checkPassword():
                self.__password = security.setPassword()
            else:
                security.wrongPassword()
                activated()


def main():
    '''Main loop. Starts the program off.
    '''
    global security
    init("COM3")
    security.setPassword()
    deactivated()

main()
