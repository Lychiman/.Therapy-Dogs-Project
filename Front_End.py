#Import addons to python language (WILL NOT WORK WITHOUT)
import customtkinter as ctk #Will need to install this via pip in comand prompt
from   tkinter import *
import datetime
import re
import sqlite3
from contextlib import closing




#Function that contains the Program
def Therapy_Dog_Database():

    #Defining variables to make it easier to change size of everything
    standardHeight= 30
    standardWidth= 250
    standardFont= "", 18
    standardYPadding= 10

    #Defining colour mode for the program (light or dark)
    ctk.set_appearance_mode("dark")
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


    #Defines the admin function
    def adminOptions():

        #Defines log in function
        def logIn():

            #Defines function that runs when user sucessfully logs in
            def succesfulLogIn():

                def sfhdvksd():
                    print("jhvfvfgd")

                noButton= ctk.CTkButton(
                    leftBottomFrame,
                    text= "No",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= sfhdvksd
                    )
                noButton.pack(pady= standardYPadding, padx= 10, side='left')
                    

            password = "Testing123"
            userEntry= passwordEntry.get()

            if userEntry != password:

                #Creates a ctk window
                passwordErrorWindow= ctk.CTkToplevel(passwordWindow)
                passwordErrorWindow.title("Error Window")
                passwordErrorWindow.geometry("500x100")
                passwordErrorWindow.transient(passwordWindow)
                passwordErrorWindow.lift()

                #Creates a ctk label
                passwordErrorLabel= ctk.CTkLabel(
                    passwordErrorWindow,
                    text= "Incorect password. Close this window and try again.",
                    font= standardFont
                    )
                passwordErrorLabel.pack(pady= standardYPadding)

                #Creates a ctk button
                passwordErrorButton= ctk.CTkButton(
                    passwordErrorWindow,
                    text= "Close Window",
                    font= standardFont,
                    width= standardWidth,
                    height= standardHeight,
                    command= passwordErrorWindow.destroy
                    )
                passwordErrorButton.pack(pady= standardYPadding)

            if userEntry == password:
                passwordWindow.destroy()
                succesfulLogIn()

        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates a ctk window
        passwordWindow= ctk.CTkToplevel(root)
        passwordWindow.title("Error Window")
        passwordWindow.geometry("500x300")
        passwordWindow.transient(root)
        passwordWindow.lift()

        for widgets in passwordWindow.winfo_children():
            widgets.destroy()

        #Creates a ctk label
        passwordLabel= ctk.CTkLabel(
            passwordWindow,
            text= "Please Enter the Admin Pasword",
            font= standardFont
            )
        passwordLabel.pack(pady= standardYPadding)

        #Creates a ctk entry box
        passwordEntry= ctk.CTkEntry(
            passwordWindow,
            placeholder_text="Enter Pasword",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            )
        passwordEntry.pack(pady= standardYPadding)

        #Creates a ctk button
        passwordButton= ctk.CTkButton(
            passwordWindow,
            text= "Log In",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= logIn
            )
        passwordButton.pack(pady= standardYPadding)

        #Creates a ctk button
        passwordButton= ctk.CTkButton(
            passwordWindow,
            text= "Close Window",
            font= standardFont,
            width= standardWidth,
            height= standardHeight,
            command= passwordWindow.destroy
            )
        passwordButton.pack(pady= standardYPadding)

    def dog_handlers():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        Listbox_Label = ctk.CTkLabel(middleFrame, text="Dog Name, Owner First Name, Owner Last Name", font = standardFont)
        Listbox_Label.pack(pady = standardYPadding)

        #Creates listbox frame
        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
        listboxFrame.pack(pady = 50)

        #Creates listbox and inserts contents of database into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT TblDogs.Name, TblHandlers.First_Name, TblHandlers.Last_Name FROM TblDog_Handlers INNER JOIN TblDogs ON TblDog_Handlers.DogID = TblDogs.DogID INNER JOIN TblHandlers ON TblDog_Handlers.HandlerID = TblHandlers.HandlerID").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(', '.join(map(str, row)))
        for row in formatted_data:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

        def details():
            
            for widgets in rightFrame.winfo_children():
                widgets.destroy()

            #Creates listbox frame
            listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
            listboxFrame.pack(pady = 50)

            #Creates listbox and inserts contents of database into it
            namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
            cursor = connection.cursor()
            data = cursor.execute("SELECT Dog_breed,Age,Special_Considerations FROM TblDogs").fetchall()
            formatted_data = []
            for row in data:
                formatted_data.append(' '.join(map(str, row)))
            for row in formatted_data:
                namesListListbox.insert(END, row)
            namesListListbox.pack(side=LEFT)

            #Creates scrollbar
            listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
            listboxScrollbar.pack(side="right", fill=Y)
            namesListListbox.config(yscrollcommand=listboxScrollbar.set)

            #Creates a button
            orderingOptionsButton = ctk.CTkButton(
                middleFrame,
                text= "Select Dog",
                font= (standardFont),
                width= standardWidth,
                height= standardHeight,
                command= details,
                )
            orderingOptionsButton.pack(pady = standardYPadding)

    def Assessments():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates listbox frame
        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
        listboxFrame.pack(pady = 50)

        #Creates listbox and inserts contents of database into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT DogID,ResultID,Date,EligibilityID FROM TblAssessments").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(' '.join(map(str, row)))
        for row in formatted_data:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

    def dog_vets():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates listbox frame
        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
        listboxFrame.pack(pady = 50)

        #Creates listbox and inserts contents of database into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT DogID,VetID FROM TblDog_Vets").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(' '.join(map(str, row)))
        for row in formatted_data:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

    def Dogs_Incidents():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates listbox frame
        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
        listboxFrame.pack(pady = 50)

        #Creates listbox and inserts contents of database into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT DogID,IncidentID FROM TblDog_Incidents").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(' '.join(map(str, row)))
        for row in formatted_data:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

    def handler_incidents():
        #Clears widgits in left bottom frame, middle frame and right frame
        for widgets in leftBottomFrame.winfo_children():
            widgets.destroy()
        for widgets in middleFrame.winfo_children():
            widgets.destroy()
        for widgets in rightFrame.winfo_children():
            widgets.destroy()

        #Creates listbox frame
        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
        listboxFrame.pack(pady = 50)

        #Creates listbox and inserts contents of database into it
        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
        cursor = connection.cursor()
        data = cursor.execute("SELECT HandlerID,IncidentID FROM TblHandler_Incidents").fetchall()
        formatted_data = []
        for row in data:
            formatted_data.append(' '.join(map(str, row)))
        for row in formatted_data:
            namesListListbox.insert(END, row)
        namesListListbox.pack(side=LEFT)

        #Creates scrollbar
        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
        listboxScrollbar.pack(side="right", fill=Y)
        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

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
        command=dog_handlers,
        )
    AACMemberOptionsButton.pack(pady = standardYPadding)

    #Creates a button
    listOfStoresButton = ctk.CTkButton(
        leftTopFrame,
        text= "Assessments",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= Assessments,
        )
    listOfStoresButton.pack(pady = standardYPadding)

    #Creates a button
    orderingOptionsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Dogs & Vets",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= dog_vets,
        )
    orderingOptionsButton.pack(pady = standardYPadding)

    #Creates a button
    storesReturnsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Dogs & Incidents",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= Dogs_Incidents,
        )
    storesReturnsButton.pack(pady = standardYPadding)

        #Creates a button
    storesReturnsButton = ctk.CTkButton(
        leftTopFrame,
        text= "Handlers & Incidents",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= handler_incidents,
        )
    storesReturnsButton.pack(pady = standardYPadding)

    #Creates a button 
    adminButton = ctk.CTkButton(
        leftTopFrame,
        text= "Admin Options",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= adminOptions,
        )
    adminButton.pack(pady = standardYPadding)
   
    #Creates a button 
    closeWindow = ctk.CTkButton(
        leftTopFrame, 
        text="Close Window", 
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= closeProgram
        )
    closeWindow.pack(pady = standardYPadding)

    #Loops through the program
    root.mainloop()

#Calls the function
Therapy_Dog_Database()