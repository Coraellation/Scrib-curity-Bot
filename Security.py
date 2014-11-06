__author__ = 'Owner'

from myro import *
import time


class Security (object):
    #This variable keeps track of the number of incorrect password attempts
    #At a certain amount, it will lock out the robot for a set number of minutes.

    def __init__(self):
        self.__startTime = time.time()
        self.__errorTime = 0
        self.__wrongTries = 0
        self.__lockedOut = False

        #GLOBAL light variables (for sensitivity)
        self.__leftS = 65000
        self.__centerS = 65300
        self.__rightS = 64600
        self.__password = []
        init("COM3")


    def setPassword(self):
        #read left, middle, right sensors
        speak ("Enter your six digit password", 0)
        self.__password = []

        while len(self.__password) < 6:
            wait(0.5)
            if getLight("left") > self.__leftS:
                password.append("L")
                print getLight("left")
                beep(.5, 800)

            elif getLight("center") > self.__centerS:
                password.append("C")
                print getLight("center")
                beep(.5, 1000)

            elif getLight("right") > self.__rightS:
                password.append("R")
                print getLight("right")
                beep(.5, 1200)
        print password

        speak("your password has been set", 0)
        return password

    def checkPassword (self):
        speak("Please enter your password.")
        for count in range(6):
            while (1):
                wait(0.5)
                if getLight("left") > self.__leftS:
                    if password[count] == "L":
                        beep(.5, 800)
                        break
                    else:
                        wrongPassword()

                elif getLight("center") > self.__centerS:
                    if password[count] == "C":
                        beep(.5, 1000)
                        break
                    else:
                        wrongPassword()

                elif getLight("right") > self.__rightS:
                    if password[count] == "R":
                        beep(.5, 1200)
                        break
                    else:
                        wrongPassword()
        wrongTries = 0
        speak("Password entered successfully. Security deactivated.")

        deactivated()

    def wrongPassword(self):
        #Sets time of first error.
        if self.__wrongTries == 0:
            self.__errorTime = time.time()

        wrongTries += 1

        if self.__wrongTries == 3 and (time.time() - self.__errorTime) < 600:
            speak("You have entered an incorrect password three times. The robot will be locked out for 10 minutes.")
            self.__lockedOut = True
            wrongTries = 0

        speak("You have entered an incorrect password", 0)
        activated()

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
