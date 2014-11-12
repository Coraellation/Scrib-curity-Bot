__author__ = 'Owner'

import Tkinter as tk

class PasswordWindow:
    def __init__(self, isGetType):
        self.ready = False
        self.window = tk.Tk()
        self.password = tk.StringVar()
        if isGetType:
            self.createGetWindow()
        else:
            self.createSetWindow()

    def createGetWindow(self):

        frame = tk.Frame()
        label = tk.Label(frame, text = "Enter your password, with a space between characters, and only L,C,R.").pack()
        entry = tk.Entry(frame, textvariable = self.password)
        entry.pack()
        button = tk.Button(frame, text = "Set Password", command = self.readyToReturn).pack()
        frame.pack()
        #STUFF
        self.window.title("Scribcurity Password Creation")
        self.window.geometry("800x500+320+220")
        self.window.mainloop()


    def createSetWindow(self):

        frame = tk.Frame()
        label = tk.Label(frame, text = "Enter your password, with a space between characters, and only L,C,R.").pack()
        entry = tk.Entry(frame, textvariable = self.password)
        entry.pack()
        button = tk.Button(frame, text = "Set Password", command = self.readyToReturn).pack()
        frame.pack()
        #STUFF
        self.window.title("Scribcurity Password Creation")
        self.window.geometry("800x500+320+220")
        self.window.mainloop()

    def readyToReturn(self):
        self.ready = True
        self.window.quit()

    def returnPassword(self):
        name = self.password.get().split()
        return name

    def destroy(self):
        try:
            self.window.destroy()
        except tk.TclError:
            pass

class GUI:
    def __init__(self):
        self.firstRun = True
        self.isCheckPassword = False
        self.isSetPassword = False
        self.isActivated = False
        self.wantActivation = False
        self.wantDeactivation = True
        self.mainMenu() #Remove this for final call.



    def mainMenu(self):
        self.menu = tk.Tk()

        logoFrame = tk.Frame()
        logo = tk.PhotoImage(file="logo.gif")
        showLogo = tk.Label(logoFrame, image = logo).pack()
        logoFrame.pack()

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

        self.menu.title("Scribcurity Welcome Page")
        self.menu.geometry("800x500+320+220")
        self.menu.mainloop()

    def setPassword(self):
        self.menu.destroy()
        self.isSetPassword = True

        window = PasswordWindow(0)
        newPass = window.returnPassword()
        print (newPass)

        window.destroy()

        self.isSetPassword = False
        self.mainMenu()

        return newPass




    def checkPassword(self, password = None):
        self.menu.destroy()
        self.isCheckPassword = True

        window = PasswordWindow(1)
        if window == password:
            window.destroy()
            self.mainMenu()
            self.isCheckPassword = False
            return True
        else:
            window.destroy()
            self.mainMenu()
            self.isCheckPassword = False
            return False



    def activate(self):
        self.menu.destroy()
        self.isActivated = not self.isActivated
        self.wantActivation = True


        wait(1)
        self.wantActivation = False
        self.mainMenu()

    def deactivate(self):
        self.menu.destroy()
        self.wantDeactivation = True
        self.isActivated = not self.isActivated

        wait(1)
        self.wantDeactivation = False
        self.mainMenu()

    def getSetPassword(self):
        return self.isSetPassword

    def getCheckPassword(self):
        return self.isCheckPassword

    def getWantActivation(self):
        return self.wantActivation

    def getWantDeactivation(self):
        return self.wantDeactivation

gui = GUI()
