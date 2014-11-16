from myro import *
import Security
import GUI


class Scribcurity:
    def __init__(self):
        self.security = Security.Security()
        self.gui = GUI.GUI()

        init("/dev/tty.Fluke2-0521-Fluke2")
        #init("COM3")
        #OR GUI ACTIVATION...
        speak ("You can now set your password on the Robot or via the GUI. To set it on the robot, use any sensor.")
        while True:
            wait(0.5)
            if (getLight("left") < self.security.getLeftS() or getLight("center") < self.security.getCenterS() or getLight("right") < self.security.getRightS()):
                self.security.setPassword()
                break
            elif self.gui.getSetPassword():
                self.security.setGUIPassword(self.gui.setPassword())
                break
        self.deactivated()

    def activated(self):
        '''This runs while the robot is activated.
        It checks to see if the user wants to deactivate the system.
        '''
        #insert sensor checking for objects
        speak("Security is now activated, to deactivate, cover the left light sensor.")

        #If the left sensor is covered, go to password entry.
        while (1):
            wait(0.5)
            print getLight()
            if getLight ("left") < self.security.getLeftS():
                #If it's not locked out, it allows for deactivation
                if not self.security.getLockedOut():
                    if self.security.checkPassword():
                        self.deactivated()
                    else:
                        self.security.wrongPassword()
                else:
                    speak("You have been locked out.")
            elif self.gui.getCheckPassword():
                if not self.security.getLockedOut():
                    if self.gui.checkPassword(self.security.getPassword()):
                        self.deactivated()
                    else:
                        self.security.wrongPassword()
                else:
                    speak("You have been locked out.")


            self.security.checkLockedOut()


    def deactivated(self):
        '''This runs while the robot is deactivated.
        Checks to see if the user wants to activate the system
        or change the password.
        '''

        speak("The robot is ready to be activated.", 0)
        speak("To activate, cover left light sensor.", 0)
        speak("To change password, cover the center light sensor.", 0)

        while(1):
            wait(0.5)
            #If the left sensor is covered, it activates
            if getLight("left") < self.security.getLeftS() or self.gui.getWantActivation():
                self.activated()

            #If the center sensor is covered, you can change your password
            if getLight("center") < self.security.getCenterS():
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
