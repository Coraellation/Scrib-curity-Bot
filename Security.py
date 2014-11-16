from myro import *
import time


class Security (object):
    def __init__(self):
        '''
        initializes the Security class
        :return: nothing
        '''
        #Times
        self.__startTime = time.time()
        self.__errorTime = 0
        self.__lockOutTime = 0

        #This variable keeps track of the number of incorrect password attempts
        #At a certain amount, it will lock out the robot for a set number of minutes
        self.__wrongTries = 0
        self.__lockedOut = False

        #GLOBAL light variables (for sensitivity)
        self.__leftS = 50000
        self.__centerS = 50000
        self.__rightS = 50000
        self.__password = []
        init("COM3")

    def getPassword(self):
        return self.__password

    def getLeftS(self):
        '''
        :return: sensitivity of the left light sensor.
        '''
        return self.__leftS

    def getCenterS(self):
        '''

        :return: sensitivity of the center light sensor.
        '''
        return self.__centerS

    def getRightS(self):
        """

        :return: sensitivity of the right light sensor.
        """
        return self.__rightS

    def setPassword(self):
        '''Sets the password for the robot.
        Takes no inputs and returns nothing.
        '''
        #read left, middle, right sensors
        speak("Enter your six digit password", 0)
        self.__password = []

        while len(self.__password) < 6:
            wait(0.5)
            if getLight("left") < self.getLeftS():
                self.__password.append("L")
                print getLight("left")
                beep(.5, 800)

            elif getLight("center") < self.getCenterS():
                self.__password.append("C")
                print getLight("center")
                beep(.5, 1000)

            elif getLight("right") < self.getRightS():
                self.__password.append("R")
                print getLight("right")
                beep(.5, 1200)
        print self.__password

        speak("your password has been set", 0)

    def setGUIPassword(self, password):
        self.__password = password

    def checkPassword (self):
        '''
        Checks if the password is correct.

        :return: 1 if the password is correct, 0 otherwise.
        '''
        speak("Please enter your password.")
        for count in range(6):
            while 1:
                wait(0.5)
                if getLight("left") < self.getLeftS():
                    if self.__password[count] == "L":
                        beep(.5, 800)
                        break
                    else:
                        return 0

                elif getLight("center") < self.getCenterS():
                    if self.__password[count] == "C":
                        beep(.5, 1000)
                        break
                    else:
                        return 0

                elif getLight("right") < self.getRightS():
                    if self.__password[count] == "R":
                        beep(.5, 1200)
                        break
                    else:
                        return 0
        self.__wrongTries = 0
        speak("Password entered successfully. Security deactivated.",0)

        return 1

    def getLockedOut(self):
        '''
        :return: self.__locked out - boolean representing if the system is locked out or not
        '''

        return self.__lockedOut

    def checkLockedOut(self):
        '''
        Checks to see if the system is still locked out by comparing the
        difference in time between the time it was locked out and the current time.
        If it has been more than 10 minutes, it unlocks the robot.
        :return:
        '''

        if time.time() - self.__lockOutTime > 600:
            self.__lockedOut = False

    def wrongPassword(self):
        '''
        Runs if the password that was entered is incorrect.
        It increments the wrongTries counter, and if it is equal to 3,
        the robot is "locked-out" and any password attempts cannot be made
        for 10 minutes. It also resets the counter for the future.
        :return:
        '''

        #Sets time of first error.
        if self.__wrongTries == 0:
            self.__errorTime = time.time()

        self.__wrongTries += 1

        if self.__wrongTries == 3 and (time.time() - self.__errorTime) < 600:
            speak("You have entered an incorrect password three times. The robot will be locked out for 10 minutes.")
            self.__lockedOut = True
            self.__wrongTries = 0

        speak("You have entered an incorrect password", 0)

