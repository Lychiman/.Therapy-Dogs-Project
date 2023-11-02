#Import addons to python language (WILL NOT WORK WITHOUT)
import customtkinter as ctk #Will need to install this via pip in comand prompt
from   tkinter import *
import datetime
import re
import sqlite3
from contextlib import closing

def Therapy_Dog_Database():

    #Defining variables to make it easier to change size of everything
    standardHeight= 30
    standardWidth= 250
    standardFont= "", 18
    standardYPadding= 10

    #Defining colour mode for the program (light or dark)
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")
    #Setting program main window
    root = ctk.CTk()
    root.title("Therapy Dog Database")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")
    root.state('zoomed')

    connection = sqlite3.connect("Testing.db")

    #Creating the frames the widgits sit in
    mainFrame = ctk.CTkFrame(root)
    mainFrame.pack(fill="both",expand=True)
    leftFrame = ctk.CTkFrame(mainFrame)
    leftFrame.pack(side='left', fill="both",expand=True)
    leftTopFrame = ctk.CTkFrame(leftFrame, fg_color= "#1f1f1f")
    leftTopFrame.pack(fill="both",expand=True)
    leftBottomFrame = ctk.CTkFrame(leftFrame, fg_color= "#292929")
    leftBottomFrame.pack(fill="both",expand=True)
    middleFrame = ctk.CTkFrame(mainFrame)
    middleFrame.pack(side='left', fill="both",expand=True)
    rightFrame = ctk.CTkFrame(mainFrame)
    rightFrame.pack(side='left', fill="both",expand=True)


    def Dog_handlers():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        label = ctk.CTkLabel(middleFrame, text="Dog Name, Owner First Name, Owner Last Name", fg_color="transparent")
        label.pack(pady = standardYPadding)


    #Defines the function to close the program
    def closeProgram():
        #Closes database connection and the program
        with closing(sqlite3.connect("Testing.db")) as connection:
            root.destroy()

    #Creates a label
    startLabel = ctk.CTkLabel(leftTopFrame, text="MADE BY Luke Roecker \nFOR USE BY AUTHORISED PERSONAL ONLY", font = standardFont)
    startLabel.pack(pady = standardYPadding)

    #Creates a button
    AACMemberOptionsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Dogs & Handlers",
        font= standardFont,
        width= standardWidth,
        height= standardHeight,
        command=Dog_handlers,
        )
    AACMemberOptionsButton.pack(pady = standardYPadding)

    #Creates a button
    AACMemberOptionsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Close Window",
        font= standardFont,
        width= standardWidth,
        height= standardHeight,
        command=closeProgram,
        )
    AACMemberOptionsButton.pack(pady = standardYPadding)

    #Loops through the program
    root.mainloop()

#Calls the function
Therapy_Dog_Database()