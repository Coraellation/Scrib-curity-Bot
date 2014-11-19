__author__ = 'Owner'

from Tkinter import *

import Tkinter as tk
import tkFont
import Security

# noinspection PyPep8Naming,PyUnusedLocal
class PasswordWindow:
    def __init__(self, isGetType, isBadPassword = False):
        self.window = tk.Tk()
        self.password = tk.StringVar()
        self.customFont = tkFont.Font(family="Helvetica light", size=16)
        self.isBadPassword = isBadPassword
        if isGetType:
            self.createGetWindow()
        else:
            self.createSetWindow()

    def createGetWindow(self):

        frame = tk.Frame()
        logoFrame = tk.Frame()
        img = tk.PhotoImage(file="passConfig.gif")
        showLogo = tk.Label(logoFrame, image = img).pack()
        logoFrame.pack()

        label = tk.Label(frame, text = "Enter your password, with a space between characters, and only L,C,R.").pack()
        entry = tk.Entry(frame, textvariable = self.password)
        entry.pack()
        button = tk.Button(frame, text = "Check Password", command = self.readyToReturn, padx = 30, pady = 40).pack()
        frame.pack()
        #STUFF
        self.window.title("Scribcurity Password Creation")
        self.window.configure()
        self.window.geometry("800x500+320+220")
        self.window.mainloop()


    def createSetWindow(self):

        frame = tk.Frame()
        logoFrame = tk.Frame()
        img = tk.PhotoImage(file="passConfig.gif")
        showLogo = tk.Label(logoFrame, image = img).pack()
        logoFrame.pack()
        label = tk.Label(frame, text = "Enter your password, with a space between characters, and only L,C,R.").pack()



        entry = tk.Entry(frame, textvariable = self.password)
        entry.pack()

        if self.isBadPassword:
            errorLabel = tk.Label (frame, text = "Error. Your password must only contain L, C, or R").pack()


        errorLabel = tk.Label (frame, text = "Error. Your password must only contain L, C, or R").pack()

        button = tk.Button(frame, text = "Set Password", command = self.readyToReturn, padx = 30, pady = 40).pack()
        frame.pack()
        #STUFF
        self.window.title("Scribcurity Password Creation")
        self.window.geometry("800x500+320+220")
        self.window.mainloop()



    #------------------------ HELPERS ---------------------------------
    def readyToReturn(self):
        self.window.quit()

    def returnPassword(self):
        name = self.password.get().split()
        return name

    def destroy(self):
        try:
            self.window.destroy()
        except tk.TclError:
            pass


# noinspection PyUnusedLocal,PyPep8Naming
class GUI:
    def __init__(self):
        self.firstRun = True
        self.isCheckPassword = False
        self.isSetPassword = False
        self.isActivated = False
        self.password = []

        self.security = Security.Security()
        self.mainMenu()
    def mainMenu(self):
        #bgCol = '#cf2d27'
        bgCol = '#ffffff'

        self.menu = tk.Tk()
        self.menu.configure(bg = bgCol)

        logoFrame = tk.Frame()
        self.customFont = tkFont.Font(family="helvetica light", size=16)

        logo = tk.PhotoImage(file="logo.gif")
        showLogo = tk.Label(logoFrame, image = logo).pack()
        logoFrame.pack()

        buttonFrame = tk.Frame(bg = bgCol)

        if self.firstRun:
            welcome = "Welcome to the Scribcurity bot user interface! You can interact with the bot" \
                      " using this computer or using the robot's sensors. For now, let's set a password " \
                      "for the robot. Click below to set it using the computer, or you can start typing " \
                      "it in on the robot directly if you'd like.\n"
            firstMessageFrame = tk.Frame()
            firstMessageFrame.config(bg=bgCol)
            firstMessageLabel = tk.Label(firstMessageFrame, text = welcome, wraplength = 600, font=self.customFont,
                                         fg = 'black', bg = bgCol).pack()
            firstMessageFrame.pack()

            activateStatus = "disabled"
            deactivateStatus = "disabled"
            password = tk.Button(buttonFrame, text = "Set Password", command = self.setPassword, padx = 30, pady = 40).pack(side =LEFT)

            self.firstRun = False

        elif self.isActivated:
            activateStatus = "disabled"
            deactivateStatus = "normal"
            password = tk.Button(buttonFrame, text = "Change Password", command = self.changePassword,padx = 20, pady = 40).pack(side = LEFT)

        else:
            activateStatus = "normal"
            deactivateStatus = "disabled"
            password = tk.Button(buttonFrame, text = "Change Password", command = self.changePassword, padx = 20, pady = 40).pack(side = LEFT)


        activate = tk.Button(buttonFrame, text = "Activate Security", command = self.activate,
                             state = activateStatus, padx = 20, pady = 40).pack(side = LEFT)
        deactivate = tk.Button(buttonFrame, text = "Deactivate Security", command = self.deactivate,
                               state = deactivateStatus, padx = 10, pady = 40).pack(side = LEFT)

        buttonFrame.pack()

        self.menu.title("Scribcurity Welcome Page")
        self.menu.geometry("800x500+320+220")
        self.menu.mainloop()

    def closeMenu(self):
        try:
            self.menu.destroy()
        except TclError:
            pass

    def setPassword(self):
        def validPasswordCheck(password):
            for i in password:
                if 'LCR '.find(i) == -1:
                #if i!='L' or i!='C' or i!='R' or i!=' ':
                    print ("invalid letters")
                    return False
            return True

        self.closeMenu()
        self.isSetPassword = True

        badPass = False
        while (1):
            if badPass:
                window = PasswordWindow(0, True)
                newPass = window.returnPassword()
            else:
                window = PasswordWindow(0)
                newPass = window.returnPassword()

            if validPasswordCheck(newPass):
                self.programPassword(newPass)
                window.destroy()
                break
            else:
                badPass = True
            window.destroy()

        self.isSetPassword = False
        self.mainMenu()

        return newPass

    def checkPassword(self):
        self.closeMenu()

        self.isCheckPassword = True

        window = PasswordWindow(1)
        newPass = window.returnPassword()
        print newPass
        if newPass == self.password:
            window.destroy()
            self.isCheckPassword = False
            return True

        else:
            window.destroy()
            self.isCheckPassword = False
            return False

    def changePassword(self):
        self.closeMenu()

        if self.checkPassword():
            self.setPassword()
        else:
            self.activate()

    def activate(self):
        self.closeMenu()
        self.isActivated = True
        self.mainMenu()

    def deactivate(self):
        self.closeMenu()
        if self.checkPassword():
            self.isActivated = False
        self.mainMenu()

    def getActivated(self):
        return self.isActivated

    def programPassword(self, password):
        self.password = password

gui = GUI()
