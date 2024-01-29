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
    middleTopFrame = ctk.CTkFrame(middleFrame, fg_color= "#292929")
    middleTopFrame.pack(fill="both",expand=True)
    middleBottomFrame = ctk.CTkFrame(middleFrame, fg_color= "#292929")
    middleBottomFrame.pack(fill="both",expand=True)
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

                    def dogs():

                        #Clears widgits in left bottom frame, middle frame and right frame
                        for widgets in leftBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleTopFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        def details():
                            
                            for widgets in middleTopFrame.winfo_children():
                                widgets.destroy()
                            for widgets in middleBottomFrame.winfo_children():
                                widgets.destroy()
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                            rowSelection = namesListListbox.curselection()

                            if rowSelection:
                                rowIndex = rowSelection[0]
                                row = formatted_data[rowIndex]
                                rowString= str(row)
                                DogID = rowString.split()[0]
                                Name = rowString.split()[2]
                                print(DogID) #ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                                print(Name) #fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

                                def Schedule():
                                    for widgets in middleBottomFrame.winfo_children():
                                        widgets.destroy()
                                    for widgets in rightFrame.winfo_children():
                                            widgets.destroy()

                                    def back():
                                        for widgets in middleBottomFrame.winfo_children():
                                            widgets.destroy()
                                        for widgets in rightFrame.winfo_children():
                                            widgets.destroy()

                                    #Creates listbox frame
                                    listboxFrame= ctk.CTkFrame(rightFrame, fg_color= "#292929")
                                    listboxFrame.pack(pady = 50)

                                    #cursor = connection.cursor()
                                    #cursor.execute("SELECT Name FROM TblDogs WHERE DogID = ?", (DogID,))
                                    #data = cursor.fetchall()
                                    data = Name

                                    dog_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text = f"Schedule - {data}",
                                        font= standardFont
                                        )
                                    dog_Label.pack(pady= standardYPadding)


                                    cursor = connection.cursor()
                                    cursor.execute("SELECT Monday FROM TblSchedule WHERE DogID = ?", (DogID,))
                                    data = cursor.fetchall()

                                    monday_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Monday - {data}",
                                        font= standardFont
                                    )
                                    monday_Label.pack(pady= standardYPadding)

                                    cursor = connection.cursor()
                                    cursor.execute("SELECT Tuesday FROM TblSchedule WHERE DogID = ?", (DogID,))
                                    data = cursor.fetchall()

                                    tuesday_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Tuesday - {data}",
                                        font= standardFont
                                        )
                                    tuesday_Label.pack(pady= standardYPadding)

                                    cursor = connection.cursor()
                                    cursor.execute("SELECT Wednesday FROM TblSchedule WHERE DogID = ?", (DogID,))
                                    data = cursor.fetchall()

                                    Wednesday_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Wednesday - {data}",
                                        font= standardFont
                                        )
                                    Wednesday_Label.pack(pady= standardYPadding)

                                    cursor = connection.cursor()
                                    cursor.execute("SELECT Thursday FROM TblSchedule WHERE DogID = ?", (DogID,))
                                    data = cursor.fetchall()

                                    thursday_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Thursday - {data}",
                                        font= standardFont
                                        )
                                    thursday_Label.pack(pady= standardYPadding)

                                    cursor = connection.cursor()
                                    cursor.execute("SELECT Friday FROM TblSchedule WHERE DogID = ?", (DogID,))
                                    data = cursor.fetchall()

                                    friday_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Friday - {data}",
                                        font= standardFont
                                        )
                                    friday_Label.pack(pady= standardYPadding)

                                    BackButton = ctk.CTkButton(
                                        listboxFrame,
                                        text= "Back",
                                        font= (standardFont),
                                        width= standardWidth,
                                        height= standardHeight,
                                        command= back,
                                        )
                                    BackButton.pack(pady = standardYPadding)

                                #Creates listbox frame
                                listboxFrame= ctk.CTkFrame(middleTopFrame, fg_color= "#292929")
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
                                    command= Schedule,
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


                        Listbox_Label = ctk.CTkLabel(leftBottomFrame, text="Dog Name, Owner First Name, Owner Last Name", font = (standardFont,25))
                        Listbox_Label.pack(pady = standardYPadding)

                        #Creates listbox frame
                        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
                        listboxFrame.pack(pady = 10)

                        #Creates listbox and inserts contents of database into it
                        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=20, font= standardFont)
                        cursor = connection.cursor()
                        data = cursor.execute("SELECT TblDogs.DogID, TblDogs.Name, TblHandlers.First_Name, TblHandlers.Last_Name FROM TblDog_Handlers INNER JOIN TblDogs ON TblDog_Handlers.DogID = TblDogs.DogID INNER JOIN TblHandlers ON TblDog_Handlers.HandlerID = TblHandlers.HandlerID").fetchall()
                        formatted_data = []
                        for row in data:
                            formatted_data.append(' - '.join(map(str, row)))
                        for row in formatted_data:
                            namesListListbox.insert(END, row)
                        namesListListbox.pack(side=LEFT)

                        #Creates scrollbar
                        listboxScrollbar= ctk.CTkScrollbar(listboxFrame, command=namesListListbox.yview)
                        listboxScrollbar.pack(side="right", fill=Y)
                        namesListListbox.config(yscrollcommand=listboxScrollbar.set)

                        details_button = ctk.CTkButton(
                        leftBottomFrame,
                        text= "Select Dog",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=details,
                        )
                        details_button.pack(pady = standardYPadding)


                    def handlers():

                        #Clears widgits in left bottom frame, middle frame and right frame
                        for widgets in leftBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleTopFrame.winfo_children():
                            widgets.destroy()
                        for widgets in middleBottomFrame.winfo_children():
                            widgets.destroy()
                        for widgets in rightFrame.winfo_children():
                            widgets.destroy()

                        def emergency_contact_info():
                            for widgets in middleBottomFrame.winfo_children():
                                widgets.destroy()
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                            

                        def incident_info():
                            for widgets in middleBottomFrame.winfo_children():
                                widgets.destroy()
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                        def veiw_dogs():
                            for widgets in middleBottomFrame.winfo_children():
                                widgets.destroy()
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                        def details():
                            for widgets in middleTopFrame.winfo_children():
                                widgets.destroy()
                            for widgets in middleBottomFrame.winfo_children():
                                widgets.destroy()
                            for widgets in rightFrame.winfo_children():
                                widgets.destroy()

                            rowSelection = namesListListbox.curselection()

                            if rowSelection:
                                rowIndexRank = rowSelection[0]
                                rowRank = formatted_data[rowIndexRank]
                                rowRankString= str(rowRank)
                                HandlerID = rowRankString.split()[0]
                            
                                #Creates listbox frame
                                listboxFrame= ctk.CTkFrame(middleTopFrame, fg_color= "#292929")
                                listboxFrame.pack(pady = 50)

                                cursor = connection.cursor()
                                cursor.execute("SELECT TblHandlers.First_Name, TblHandlers.Last_Name FROM TblHandlers WHERE HandlerID = ?", (HandlerID,))
                                data = cursor.fetchone()
                                if data:
                                    formatted_name = ' '.join(map(str, data))

                                    name_Label = ctk.CTkLabel(
                                        listboxFrame,
                                        text=formatted_name,
                                        font=(standardFont,50)
                                    )
                                    name_Label.pack(pady=standardYPadding)
                                else:
                                    # Handle the case where no data was found for the given HandlerID
                                    error_name_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= "Error: No Data Found",
                                        font= standardFont
                                    )
                                    error_name_Label.pack(pady= standardYPadding)

                                cursor = connection.cursor()
                                cursor.execute("SELECT TblHandlers.Phone_Number FROM TblHandlers WHERE HandlerID = ?", (HandlerID,))
                                data = cursor.fetchone()
                                if data:
                                    phone_number = ''.join(map(str, data))
                                    formatted_number = "0" + phone_number

                                    phone_number_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= formatted_number,
                                        font= standardFont
                                        )
                                    phone_number_Label.pack(pady= standardYPadding)
                                else:
                                    # Handle the case where no data was found for the given HandlerID
                                    error_number_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= "Error: No Data Found",
                                        font= standardFont
                                    )
                                    error_number_Label.pack(pady= standardYPadding)

                                cursor = connection.cursor()
                                cursor.execute("SELECT TblHandlers.Email_Address FROM TblHandlers WHERE HandlerID = ?", (HandlerID,))
                                data = cursor.fetchone()
                                if data:
                                    formatted_number = ' '.join(map(str, data))

                                    email_address_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= formatted_number,
                                        font= standardFont
                                        )
                                    email_address_Label.pack(pady= standardYPadding)
                                else:
                                    # Handle the case where no data was found for the given HandlerID
                                    error_email_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= "Error: No Data Found",
                                        font= standardFont
                                    )
                                    error_email_Label.pack(pady= standardYPadding)

                                cursor = connection.cursor()
                                cursor.execute("SELECT TblHandlers.Street_Number, TblHandlers.Street_Name, TblHandlers.'Suburb/City', TblHandlers.Post_Code, TblStates.State, TblHandlers.Country FROM TblHandlers INNER JOIN TblStates ON TblHandlers.StateID = TblStates.StateID WHERE HandlerID = ? ", (HandlerID,))
                                data = cursor.fetchone()
                                if data:
                                    formatted_number = ' '.join(map(str, data))

                                    address_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= formatted_number,
                                        font= standardFont
                                        )
                                    address_Label.pack(pady= standardYPadding)
                                else:
                                    # Handle the case where no data was found for the given HandlerID
                                    error_address_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= "Error: No Data Found",
                                        font= standardFont
                                    )
                                    error_address_Label.pack(pady= standardYPadding)

                                cursor = connection.cursor()
                                cursor.execute("SELECT COUNT(*) FROM TblHandler_Incidents WHERE HandlerID = ?", (HandlerID,))
                                data = cursor.fetchone()
                                if data:
                                    formatted_number = ' '.join(map(str, data))

                                    Incident_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= f"Incident Count: {formatted_number}",
                                        font= standardFont
                                        )
                                    Incident_Label.pack(pady= standardYPadding)
                                else:
                                    # Handle the case where no data was found for the given HandlerID
                                    error_Incident_Label= ctk.CTkLabel(
                                        listboxFrame,
                                        text= "Error: No Data Found",
                                        font= standardFont
                                    )
                                    error_Incident_Label.pack(pady= standardYPadding)

                                #Creates a button
                                Handler_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View emergency contact Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= emergency_contact_info,
                                    )
                                Handler_InformationButton.pack(pady = standardYPadding)

                                Veiw_Dogs_Button = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View incident Information",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= incident_info,
                                    )
                                Veiw_Dogs_Button.pack(pady = standardYPadding)

                                incident_InformationButton = ctk.CTkButton(
                                    listboxFrame,
                                    text= "View Dogs",
                                    font= (standardFont),
                                    width= standardWidth,
                                    height= standardHeight,
                                    command= veiw_dogs,
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

                        Listbox_Label = ctk.CTkLabel(leftBottomFrame, text="Handlers", font =(standardFont, 25))
                        Listbox_Label.pack(pady = standardYPadding)

                        #Creates listbox frame
                        listboxFrame= ctk.CTkFrame(leftBottomFrame, fg_color= "#292929")
                        listboxFrame.pack(pady = 10)

                        #Creates listbox and inserts contents of database into it
                        namesListListbox = Listbox(listboxFrame, bg= "#292929", fg= "Silver", width= 30, height=20, font= standardFont)
                        cursor = connection.cursor()
                        data = cursor.execute("SELECT TblHandlers.HandlerID, TblHandlers.First_Name, TblHandlers.Last_Name FROM TblHandlers").fetchall()
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

                        details_button = ctk.CTkButton(
                        leftBottomFrame,
                        text= "Select Handler",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=details,
                        )
                        details_button.pack(pady = standardYPadding)

                    for widgets in leftTopFrame.winfo_children():
                        widgets.destroy()
                    for widgets in leftBottomFrame.winfo_children():
                        widgets.destroy()
                    for widgets in middleTopFrame.winfo_children():
                        widgets.destroy()
                    for widgets in middleBottomFrame.winfo_children():
                        widgets.destroy()
                    for widgets in rightFrame.winfo_children():
                        widgets.destroy()

                    #Creates a label
                    startLabel = ctk.CTkLabel(leftTopFrame, text="MADE BY Luke Roecker \nFOR USE BY AUTHORISED PERSONAL ONLY", font = standardFont)
                    startLabel.pack(pady = standardYPadding)

                    #Creates a button
                    Dog_Button = ctk.CTkButton(
                        leftTopFrame,
                        text= "Dog Infomation",
                        font= standardFont,
                        width= standardWidth,
                        height= standardHeight,
                        command=dogs,
                        )
                    Dog_Button.pack(pady = standardYPadding)

                    #Creates a button
                    Handler_Button = ctk.CTkButton(
                        leftTopFrame,
                        text= "Handler Information",
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
                    

            password = "IDK"
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
        for widgets in middleTopFrame.winfo_children():
            widgets.destroy()
        for widgets in middleBottomFrame.winfo_children():
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
            show= '*',
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