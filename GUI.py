__author__ = 'Owner'

import tkinter as tk

class GUI (object):
    def __init__(self):
        self.firstRun = True
        self.isCheckPassword = False
        self.isSetPassword = False
        self.isActivated = False
        self.wantActivation = False
        self.wantDeactivation = True
        self.mainMenu() #Remove this for final call.


    def mainMenu(self):
        menu = tk.Tk().wm_title("Main Menu")

        buttonFrame = tk.Frame()
        if self.firstRun:
            welcome = "Welcome to the Scribcurity bot user interface! You can interact with the bot" \
                      " using this computer or using the robot's sensors. For now, let's set a password " \
                      "for the robot. Click below to set it using the computer, or you can start typing " \
                      "it in on the robot directly if you'd like."
            firstMessageFrame = tk.Frame()
            firstMessageLabel = tk.Label(firstMessageFrame, text = welcome, wraplength = 400).pack()
            firstMessageFrame.pack()

            activateStatus = "disabled"
            deactivateStatus = "disabled"
            password = tk.Button(buttonFrame, text = "Set Password", command = self.setPassword).pack()

            self.firstRun = False

        elif self.isActivated:
            activateStatus = "disabled"
            deactivateStatus = "normal"
            password = tk.Button(buttonFrame, text = "Change Password", command = self.checkPassword).pack()

        else:
            activateStatus = "normal"
            deactivateStatus = "disabled"
            password = tk.Button(buttonFrame, text = "Change Password", command = self.checkPassword).pack()


        activate = tk.Button(buttonFrame, text = "Activate Security", command = self.activate,
                             state = activateStatus).pack()
        deactivate = tk.Button(buttonFrame, text = "Decactivate Security", command = self.deactivate,
                               state = deactivateStatus).pack()

        buttonFrame.pack()
        tk.mainloop()

    def setPassword(self):
        self.isSetPassword = True

        window = tk.Tk().wm_title("Set Your Password")
        frame = tk.Frame()
        label = tk.Label(frame, text = "Enter your password, using no spaces, and only L,C,R.").pack()
        entry = tk.Entry(frame).pack()
        button = tk.Button(frame, text = "Set Password", command = ).pack()
        frame.pack()
        #STUFF
        tk.mainloop()

        self.isSetPassword = False

    def checkPassword(self):
        self.isCheckPassword = True

        #STUFF

        self.isCheckPassword = False

    def activate(self):
        self.isActivated = not self.isActivated
        self.wantActivation = True


        #STUFF

        self.wantActivation = False

    def deactivate(self):
        self.wantDeactivation = True
        self.isActivated = not self.isActivated

        #STUFF


        self.wantDeactivation = False

    def getSetPassword(self):
        return self.isSetPassword

    def getCheckPassword(self):
        return self.isCheckPassword

    def getWantActivation(self):
        return self.wantActivation

    def getWantDeactivation(self):
        return self.wantDeactivation

gui = GUI()
