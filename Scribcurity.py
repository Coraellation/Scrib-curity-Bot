import Security
import time
from myro import *

init("COM3")

class Scribcurity:
    """
    The Scribcurity class.
    The "main" class of the system - incorporates both the GUI system as well as the Scribbler bot.
    """
    def __init__(self):
        """
        Initializes the Scribcurity class.
        :return:
        """
        self.security = Security.Security()

        #OR GUI ACTIVATION...
        self.security.saySomething (
            "Light any sensor to set password.")

        #Check to see if user wants to set password
        while True:
            time.sleep(0.1)
            #If a light is detected at any sensor, set using the Scribbler
            if (self.security.returnLight("left") < self.security.getLeftS()):
                beep(.5, 800)
                self.security.setPassword()
                break
            elif (self.security.returnLight("center") < self.security.getCenterS()):
                beep(.5, 1000)
                self.security.setPassword()
                break
            elif( self.security.returnLight("right") < self.security.getRightS()):
                beep(.5, 1200)
                self.security.setPassword()
                break


        self.deactivated()

    def activated(self):
        """
        This runs while the robot is activated.
        It checks to see if the user wants to deactivate the system.
        """
        self.security.saySomething("Security system is now activated")
        self.security.startAlarm()

    #If the left sensor is lighted, go to password entry.
        beep(.5, 800)
        #If it's not locked out, it allows for deactivation
        if not self.security.getLockedOut():
            if self.security.checkPassword():
                self.deactivated()
            else:
                self.security.wrongPassword()
        else:
            self.security.saySomething("You have been locked out.")
        self.security.checkLockedOut()

    def deactivated(self):
        """
        This runs while the robot is deactivated.
        Checks to see if the user wants to activate the system
        or change the password.
        """

        self.security.saySomething("The robot is currently deactivated.")
        self.security.saySomething("To activate, light the left light sensor.")
        self.security.saySomething("To change password, light the center light sensor.")

        while True:
            time.sleep(0.1)
            #If the left sensor is lit, it activates.
            if self.security.returnLight("left") < self.security.getLeftS():
                beep(.5, 800)
                self.activated()

            #If the center sensor is lit, you can change your password
            if self.security.returnLight("center") < self.security.getCenterS() and not self.security.getLockedOut():
                #If the password is correct, sets the password.
                beep(.5, 1000)
                if self.security.checkPassword():
                    self.security.setPassword()

                #Otherwise, reactivate security.
                else:
                    self.security.wrongPassword()
                    self.activated()
        self.security.checkLockedOut()

scribcurity = Scribcurity()
