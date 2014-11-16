import Security
import GUI
import time



class Scribcurity:
    def __init__(self):
        self.security = Security.Security()
        self.gui = GUI.GUI()

        #OR GUI ACTIVATION...
        self.security.saySomething ("You can now set your password on the Robot or via the GUI. To set it on the robot, use any sensor.")
        while True:
            time.sleep(0.1)
            if (self.security.returnLight("left") < self.security.getLeftS()
                or self.security.returnLight("center") < self.security.getCenterS()
                or self.security.returnLight("right") < self.security.getRightS()):

                self.security.setPassword()
                break
            elif self.gui.getSetPassword():
                self.security.setGUIPassword(self.gui.setPassword())
                break
        self.deactivated()

    def activated(self):
        """
        This runs while the robot is activated.
        It checks to see if the user wants to deactivate the system.
        """
        #insert sensor checking for objects
        self.security.saySomething("Security is now activated, to deactivate, cover the left light sensor.")

        #If the left sensor is covered, go to password entry.
        while True:
            time.sleep(0.1)
            print self.security.returnLight()
            if self.security.returnLight ("left") < self.security.getLeftS():
                #If it's not locked out, it allows for deactivation
                if not self.security.getLockedOut():
                    if self.security.checkPassword():
                        self.deactivated()
                    else:
                        self.security.wrongPassword()
                else:
                    self.security.saySomething("You have been locked out.")
            elif self.gui.getCheckPassword():
                if not self.security.getLockedOut():
                    if self.gui.checkPassword(self.security.getPassword()):
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

        self.security.saySomething("The robot is ready to be activated.")
        self.security.saySomething("To activate, cover left light sensor.")
        self.security.saySomething("To change password, cover the center light sensor.")

        while True:
            time.sleep(0.1)
            #If the left sensor is covered, it activates
            if self.security.returnLight("left") < self.security.getLeftS() or self.gui.getWantActivation():
                self.activated()

            #If the center sensor is covered, you can change your password
            if self.security.returnLight("center") < self.security.getCenterS():
                if self.security.checkPassword():
                    self.security.setPassword()
                else:
                    self.security.wrongPassword()
                    self.activated()
            elif self.gui.getCheckPassword():
                if self.gui.checkPassword(self.security.getPassword()):
                    self.security.setGUIPassword(self.gui.setPassword())
                else:
                    self.security.wrongPassword()
                    self.activated()

scribcurity = Scribcurity()
