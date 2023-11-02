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
    
    #Defines the function to close the program
    def closeProgram():
        #Closes database connection and the program
        with closing(sqlite3.connect("Testing.db")) as connection:
            root.destroy()

    #Defines the admin function
    def userOptions():

        #Defines log in function
        def logIn():

            #Defines function that runs when user sucessfully logs in
            def succesfulLogIn():

                    def dog_handlers():
                        #Clears widgits in left bottom frame, middle frame and right frame
                        for widgets in leftBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleFrame.winfo_children():
                            widgets.destroy()
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        def details():
                            
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                            rowSelection = namesListListbox.curselection()

                            if rowSelection:
                                rowIndexRank = rowSelection[0]
                                rowRank = formatted_data[rowIndexRank]
                                rowRankString= str(rowRank)
                                DogID = rowRankString.split()[0]
                            
                                #Creates listbox frame
                                listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
                                listboxFrame.pack(pady = 50)

                                Dogname_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "dog name",
                                    font= standardFont
                                    )
                                Dogname_Label.pack(pady= standardYPadding)

                                handlername_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "handler name",
                                    font= standardFont
                                    )
                                handlername_Label.pack(pady= standardYPadding)

                                age_of_dog_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "age of dog",
                                    font= standardFont
                                    )
                                age_of_dog_Label.pack(pady= standardYPadding)

                                breed_of_dog_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "breed of dog",
                                    font= standardFont
                                    )
                                breed_of_dog_Label.pack(pady= standardYPadding)
                                
                                number_of_incidents_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "number of incidents",
                                    font= standardFont
                                    )
                                number_of_incidents_Label.pack(pady= standardYPadding)

                                #Creates a button
                                
                                schedule_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View Schedule",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                schedule_InformationButton.pack(pady = standardYPadding)

                                #Creates a button
                                Handler_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View Handler Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                Handler_InformationButton.pack(pady = standardYPadding)

                                incident_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View incident Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                incident_InformationButton.pack(pady = standardYPadding)

                                Vet_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View vet Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                Vet_InformationButton.pack(pady = standardYPadding)

                                Assessment_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View All Assessments",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                Assessment_InformationButton.pack(pady = standardYPadding)

                            else:
                                #Creates error window
                                errorWindow= ctk.CTkToplevel(root)
                                errorWindow.title("Error Window")
                                errorWindow.geometry("500x200")
                                errorWindow.transient(root)
                                errorWindow.lift()

                                #Creates label
                                errorLabel= ctk.CTkLabel(
                                    errorWindow,
                                    text= "Please select a dog",
                                    font= standardFont
                                    )
                                errorLabel.pack(pady= standardYPadding)

                                #Creates button to close window
                                errorButton= ctk.CTkButton(
                                    errorWindow,
                                    text= "Close Window",
                                    font= standardFont,
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= errorWindow.destroy
                                    )
                                errorButton.pack(pady= standardYPadding)

                        Listbox_Label = ctk.CTkLabel(middleFrame, text="Dog Name, Owner First Name, Owner Last Name", font = standardFont)
                        Listbox_Label.pack(pady = standardYPadding)

                        details_button = ctk.CTkButton(
                        middleFrame,
                        text= "Select Dog",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=details,
                        )
                        details_button.pack(pady = standardYPadding)

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

                    def handlers():
                        #Clears widgits in left bottom frame, middle frame and right frame
                        for widgets in leftBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleFrame.winfo_children():
                            widgets.destroy()
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        def details():
                            
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                            rowSelection = namesListListbox.curselection()

                            if rowSelection:
                                rowIndexRank = rowSelection[0]
                                rowRank = formatted_data[rowIndexRank]
                                rowRankString= str(rowRank)
                                DogID = rowRankString.split()[0]
                            
                                #Creates listbox frame
                                listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
                                listboxFrame.pack(pady = 50)

                                name_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "Handler Name",
                                    font= standardFont
                                    )
                                name_Label.pack(pady= standardYPadding)


                                phone_number_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "phone number",
                                    font= standardFont
                                    )
                                phone_number_Label.pack(pady= standardYPadding)

                                email_address_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "email address",
                                    font= standardFont
                                    )
                                email_address_Label.pack(pady= standardYPadding)

                                address_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "address",
                                    font= standardFont
                                    )
                                address_Label.pack(pady= standardYPadding)
                                
                                number_of_incidents_Label= ctk.CTkLabel(
                                    listboxFrame,
                                    text= "number of incidents",
                                    font= standardFont
                                    )
                                number_of_incidents_Label.pack(pady= standardYPadding)

                                #Creates a button
                                Handler_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View emergency contact Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                Handler_InformationButton.pack(pady = standardYPadding)

                                incident_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View incident Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= details,
                                    )
                                incident_InformationButton.pack(pady = standardYPadding)

                            else:
                                #Creates error window
                                errorWindow= ctk.CTkToplevel(root)
                                errorWindow.title("Error Window")
                                errorWindow.geometry("500x200")
                                errorWindow.transient(root)
                                errorWindow.lift()

                                #Creates label
                                errorLabel= ctk.CTkLabel(
                                    errorWindow,
                                    text= "Please select a Handler",
                                    font= standardFont
                                    )
                                errorLabel.pack(pady= standardYPadding)

                                #Creates button to close window
                                errorButton= ctk.CTkButton(
                                    errorWindow,
                                    text= "Close Window",
                                    font= standardFont,
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= errorWindow.destroy
                                    )
                                errorButton.pack(pady= standardYPadding)

                        Listbox_Label = ctk.CTkLabel(middleFrame, text="First Name,Last Name", font = standardFont)
                        Listbox_Label.pack(pady = standardYPadding)

                        details_button = ctk.CTkButton(
                        middleFrame,
                        text= "Select Handler",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=details,
                        )
                        details_button.pack(pady = standardYPadding)

                        #Creates listbox frame
                        listboxFrame= ctk.CTkFrame(middleFrame, fg_color= "#292929")
                        listboxFrame.pack(pady = 50)

                        #Creates listbox and inserts contents of database into it
                        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=40, font= standardFont)
                        cursor = connection.cursor()
                        data = cursor.execute("SELECT TblHandlers.First_Name, TblHandlers.Last_Name FROM TblHandlers").fetchall()
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

                    for widgets in leftTopFrame.winfo_children():
                        widgets.destroy()
                    for widgets in leftBottomFrame.winfo_children():
                        widgets.destroy()
                    for widgets in middleFrame.winfo_children():
                        widgets.destroy()
                    for widgets in rightFrame.winfo_children():
                        widgets.destroy()

                    #Creates a label
                    startLabel = ctk.CTkLabel(leftTopFrame, text="MADE BY Luke Roecker \nFOR USE BY AUTHORISED PERSONAL ONLY", font = standardFont)
                    startLabel.pack(pady = standardYPadding)

                    #Creates a button
                    Dog_Handler_Button = ctk.CTkButton(
                        leftTopFrame,
                        text= "Dogs",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=dog_handlers,
                        )
                    Dog_Handler_Button.pack(pady = standardYPadding)

                    #Creates a button
                    Handler_Button = ctk.CTkButton(
                        leftTopFrame,
                        text= "Handlers",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=handlers,
                        )
                    Handler_Button.pack(pady = standardYPadding)

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
            text= "Please Enter the Pasword",
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


    #Creates a label
    startLabel = ctk.CTkLabel(leftTopFrame, text="MADE BY Luke Roecker \nFOR USE BY AUTHORISED PERSONAL ONLY", font = standardFont)
    startLabel.pack(pady = standardYPadding)

    #Creates a button 
    adminButton = ctk.CTkButton(
        leftTopFrame,
        text= "Login",
        font= (standardFont),
        width= standardWidth,
        height= standardHeight,
        command= userOptions,
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