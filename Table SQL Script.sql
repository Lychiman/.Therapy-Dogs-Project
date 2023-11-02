CREATE TABLE TblResult(     /*Creates a table called TblResult*/
ResultID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,    /*creates column called ResultID as an Integer, Primary key, Not Null, and to Auto Increment*/
Result VARCHAR NOT NULL     /*Creates column called Result as a VARCHAR and Not NULL*/
);

CREATE TABLE TblStates(     /*Creates a table called TblStates*/
StateID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, /*creates column called StateID as an Integer, Primary key, Not Null, and to Auto Increment*/
State VARCHAR NOT NULL      /*Creates column called State as a VARCHAR and Not NULL*/
);

CREATE TABLE Tbl_Incidents(     /*Creates a table called Tbl_Incidents*/
IncidentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  /*creates column called IncidentID as an Integer, Primary key, Not Null, and to Auto Increment*/
Date DATE DEFAULT CURRENT_DATE NOT NULL,        /*Creates column called Date as a Date and Not NULL, with a default to Current Date*/
Description_of_Incident VARCHAR NOT NULL        /*Creates column called Description_of_Incident as a VARCHAR and Not NULL*/
);

CREATE TABLE TblEligibility(        /*Creates a table called TblEligibility*/
EligibilityID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,   /*creates column called EligibilityID as an Integer, Primary key, Not Null, and to Auto Increment*/
Eligibility VARCHAR NOT NULL        /*Creates column called Eligbility as a VARCHAR and Not NULL*/
);

CREATE TABLE TblVets(       /*Creates a table called TblVets*/
VetID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,   /*creates column called VetID as an Integer, Primary key, Not Null, and to Auto Increment*/
Vet VARCHAR NOT NULL,       /*Creates column called Vet as a VARCHAR and Not NULL*/
Street_Number INTEGER NOT NULL,     /*Creates column called Street_Number as a Integer and Not NULL*/
Street_Name VARCHAR NOT NULL,       /*Creates column called Street_Name as a VARCHAR and Not NULL*/
"Suburb/City" VARCHAR NOT NULL,     /*Creates column called Suburb/City as a VARCHAR and Not NULL*/
Post_Code INTEGER(4) NOT NULL,      /*Creates column called Postcode as a Integer with a length of 4 and Not NULL*/
StateID INTEGER NOT NULL,       /*Creates column called StateID as a Integer and Not NULL*/
Country VARCHAR NOT NULL,       /*Creates column called Country as a VARCHAR and Not NULL*/
FOREIGN KEY (StateID) References TblStates (StateID)        /*Creates a Foreign Key to link StateID from TblStates to TblVets*/
);

CREATE TABLE TblHandlers(       /*Creates a table called TblHandlers*/
HandlerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,   /*creates column called HandlerID as an Integer, Primary key, Not Null, and to Auto Increment*/
First_Name VARCHAR NOT NULL,        /*Creates column called First_Name as a VARCHAR and Not NULL*/
Last_Name VARCHAR NOT NULL,         /*Creates column called Last_Name as a VARCHAR and Not NULL*/
Phone_Number INTEGER(10) CHECK (Phone_Number >= '0400000000') NOT NULL,     /*Creates column called Phone_Number as an integer with a length of 10, NOT NULL, and with a check to make sure its in a phone number format*/
Email_Address VARCHAR NOT NULL,     /*Creates column called Email_Address as a VARCHAR and Not NULL*/
Street_Number INTEGER NOT NULL,     /*Creates column called Street_Number as a Integer and Not NULL*/
Street_Name VARCHAR NOT NULL,       /*Creates column called Street_Name as a VARCHAR and Not NULL*/
"Suburb/City" VARCHAR NOT NULL,     /*Creates column called Cuburb/City as a VARCHAR and Not NULL*/
Post_Code INTEGER(4) NOT NULL,      /*Creates column called Postcode as a Integer with a length of 4 and Not NULL*/
StateID INTEGER NOT NULL,       /*Creates column called StateID as a Integer and Not NULL*/
Country VARCHAR NOT NULL,       /*Creates column called Country as a VARCHAR and Not NULL*/
Emergency_Contact_First_Name VARCHAR NOT NULL,      /*Creates column called Emergency_Contact_First_Name as a VARCHAR and Not NULL*/
Emergency_Contact_Last_Name VARCHAR NOT NULL,       /*Creates column called Emergency_Contact_Last_Name as a VARCHAR and Not NULL*/
Emergency_Contact_Phone_Number INTEGER(10) CHECK (Phone_Number >= '0400000000') NOT NULL, /*Creates column called Emergency_Contact_Phone_Number as an integer with a length of 10, NOT NULL, and with a check to make sure its in a phone number format*/
FOREIGN KEY (StateID) References TblStates (StateID)        /*Creates a Foreign Key to link StateID from TblStates to TblHandlers*/
);

CREATE TABLE TblDogs(       /*Creates a table called TblDogs*/
DogID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,   /*creates column called DogID as an Integer, Primary key, Not Null, and to Auto Increment*/
Name VARCHAR NOT NULL,      /*Creates column called Name as a VARCHAR and Not NULL*/
Dog_breed VARCHAR NOT NULL,     /*Creates column called Dog_Breed as a VARCHAR and Not NULL*/
Age INTEGER(2) NOT NULL,        /*Creates column called Age as a Integer with a length of 2 and Not NULL*/
Special_Considerations VARCHAR      /*Creates column called Vet as a VARCHAR*/
);

CREATE TABLE TblAssessments(        /*Creates a table called TblAssessments*/
AssessmentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,    /*creates column called AssessmentID as an Integer, Primary key, Not Null, and to Auto Increment*/
DogID INTEGER NOT NULL,     /*Creates column called DogID as a Integer and Not NULL*/
ResultID INTEGER NOT NULL,  /*Creates column called ResultID as a Integer and Not NULL*/
Date DATE DEFAULT CURRENT_DATE NOT NULL,    /*Creates column called Date as a Date and Not NULL, with a default to Current Date*/
EligibilityID INTEGER,      /*Creates column called EligibilityID as a Integer*/
FOREIGN KEY (DogID) References TblDogs (DogID),     /*Creates a Foreign Key to link DogID from TblDogs to TblAssessments*/
FOREIGN KEY (ResultID) References TblResult (ResultID)      /*Creates a Foreign Key to link ResultID from TblResult to TblAssessments*/
FOREIGN KEY (EligibilityID) References TblEligibility (EligibilityID)       /*Creates a Foreign Key to link EligibilityID from TblEligibility to TblAssessments*/
);


CREATE TABLE TblDog_Vets(       /*Creates a table called TblDog_Vets*/
Dog_VetsID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  /*creates column called Dog_VetsID as an Integer, Primary key, Not Null, and to Auto Increment*/
DogID INTEGER NOT NULL,         /*Creates column called DogID as a Integer and Not NULL*/
VetID INTEGER NOT NULL,         /*Creates column called VetID as a Integer and Not NULL*/
FOREIGN KEY (DogID) References TblDogs (DogID),     /*Creates a Foreign Key to link DogID from TblDogs to TblDog_Vets*/
FOREIGN KEY (VetID) References TblVets (VetID)      /*Creates a Foreign Key to link VetID from TblVets to TblDog_Vets*/
);

CREATE TABLE TblHandler_Incidents(      /*Creates a table called TblHandler_Incidents*/
Handler_IncidentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  /*creates column called Handler_IncidentID as an Integer, Primary key, Not Null, and to Auto Increment*/
HandlerID INTEGER NOT NULL,     /*Creates column called HandlerID as a Integer and Not NULL*/
IncidentID INTEGER NOT NULL,        /*Creates column called IncidentID as a Integer and Not NULL*/
FOREIGN KEY (HandlerID) References TblHandlers (HandlerID),     /*Creates a Foreign Key to link HandlerID from TblHandlers to TblHandler_Incidents*/
FOREIGN KEY (IncidentID) References Tbl_Incidents (IncidentID)      /*Creates a Foreign Key to link IncidentID from Tbl_Incidents to TblHandler_Incidents*/
);

CREATE TABLE TblDog_Handlers(       /*Creates a table called TblDog_Handlers*/
Dog_HandlerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, /*creates column called Dog_HandlerID as an Integer, Primary key, Not Null, and to Auto Increment*/
DogID INTEGER NOT NULL,     /*Creates column called DogID as a Integer and Not NULL*/
HandlerID INTEGER NOT NULL,     /*Creates column called HandlerID as a Integer and Not NULL*/
FOREIGN KEY (DogID) References TblDogs (DogID),     /*Creates a Foreign Key to link DogID from TblDogs to TblDog_Handlers*/
FOREIGN KEY (HandlerID) References TblHandlers (HandlerID)      /*Creates a Foreign Key to link HandlerID from TblHandlers to TblDog_Handlers*/
);

CREATE TABLE TblDog_Incidents(      /*Creates a table called TblDog_Incidents*/
Dog_IncidentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  /*creates column called Dog_IncidentID as an Integer, Primary key, Not Null, and to Auto Increment*/
DogID INTEGER NOT NULL,     /*Creates column called DogID as a Integer and Not NULL*/
IncidentID INTEGER NOT NULL,        /*Creates column called IncidentID as a Integer and Not NULL*/
FOREIGN KEY (DogID) References TblDogs (DogID),     /*Creates a Foreign Key to link DogID from TblDogs to TblDog_Incidents*/
FOREIGN KEY (IncidentID) References Tbl_Incidents (IncidentID)      /*Creates a Foreign Key to link IncidentID from Tbl_Incidents to TblDog_Incidents*/
);

CREATE TABLE Tblschedule(
ScheduleID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
DogID INTEGER NOT NULL,
Monday BOOLEAN NOT NULL,
Tuesday BOOLEAN NOT NULL,
Wednesday BOOLEAN NOT NULL,
Thursday BOOLEAN NOT NULL,
Friday BOOLEAN NOT NULL,
FOREIGN KEY (DogID) References TblDogs (DogID)
);