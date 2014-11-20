from myro import *
import time
import alarm


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Security:
    """
    The Security class.
    Manages password and security features.
    Manages sensing technology as well.
    """
    def __init__(self):
        """
        initializes the Security class
        :return: nothing
        """
        #Times
        self.__startTime = time.time()
        self.__errorTime = 0
        self.__lockOutTime = 0

        #This variable keeps track of the number of incorrect password attempts
        #At a certain amount, it will lock out the robot for a set number of minutes
        self.__wrongTries = 0
        self.__lockedOut = False

        #GLOBAL light variables (for sensitivity)
        self.__leftS = 60000
        self.__centerS = 60000
        self.__rightS = 60000

        self.__password = []
        #init ("/dev/tty.Fluke2-0521-Fluke2")
        init("COM3")

    def setPassword(self):
        """
        Sets the password for the robot.
        Takes no inputs and returns nothing.
        """
        #read left, middle, right sensors
        self.saySomething("Enter your six digit password")
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

    def programPassword(self, password):
        """
        Sets the password from an external source (GUI)
        :param password: the password to be set - an array of 6 strings.
        :return: none.
        """
        self.__password = password

    def checkPassword (self):
        """
        Checks if the password is correct.

        :return: 1 if the password is correct, 0 otherwise.
        """
        self.saySomething("Please enter your password.")
        for count in range(6):
            while 1:
                wait(0.5)
                if getLight("left") < self.getLeftS():
                    beep(.5, 800)
                    if self.__password[count] == "L":
                        break
                    else:
                        return False

                elif getLight("center") < self.getCenterS():
                    beep(.5, 1000)
                    if self.__password[count] == "C":
                        break
                    else:
                        return False

                elif getLight("right") < self.getRightS():
                    beep(.5, 1200)
                    if self.__password[count] == "R":
                        break
                    else:
                        return False
        self.__wrongTries = 0
        self.saySomething("Password entered successfully. Security deactivated.")

        return True

    #-------------------------------- LOCK OUT ------------------------------------
    def getLockedOut(self):
        """
        :return: self.__locked out - boolean representing if the system is locked out or not
        """

        return self.__lockedOut

    def checkLockedOut(self):
        """
        Checks to see if the system is still locked out by comparing the
        difference in time between the time it was locked out and the current time.
        If it has been more than 10 minutes, it unlocks the robot.
        :return:
        """

        if time.time() - self.__lockOutTime > 600:
            self.__lockedOut = False

    def wrongPassword(self):
        """
        Runs if the password that was entered is incorrect.
        It increments the wrongTries counter, and if it is equal to 3,
        the robot is "locked-out" and any password attempts cannot be made
        for 10 minutes. It also resets the counter for the future.
        :return:
        """
        self.saySomething("You have entered an incorrect password")

        #If it's the first mistake - sets the time of the original mistake.
        if self.__wrongTries == 0:
            self.__errorTime = time.time()

        self.__wrongTries += 1

        if self.__wrongTries == 3 and (time.time() - self.__errorTime) < 600:
            self.saySomething("You have entered an incorrect password three times. The robot will be locked out for 10 minutes.")
            self.__lockedOut = True
            self.__wrongTries = 0


    #----------------------------------------- HELPERS ------------------------------------------
    def returnPassword(self):
        """

        :return: password stored in the security file.
        """
        return self.__password

    def getLeftS(self):
        """
        :return: sensitivity of the left light sensor.
        """
        return self.__leftS

    def getCenterS(self):
        """

        :return: sensitivity of the center light sensor.
        """
        return self.__centerS

    def getRightS(self):
        """

        :return: sensitivity of the right light sensor.
        """
        return self.__rightS

    def returnLight(self, sensor = "all"):
        """
        :param sensor: "left", "center", or "right"
        :return: reading from that sensor
        """
        return getLight(sensor)

    def saySomething(self, message):
        speak(message)

    def startAlarm(self):
        alarm.setBounds()
        alarm.placeObjects()
        while getLight("left") > self.getLeftS():
            alarm.alarmIterate()

    def startAlarmGUI(self):
        alarm.setBounds()
        alarm.placeObjects()
        while getLight("left") > self.getLeftS():
            self.security.saySomething("Activated")


