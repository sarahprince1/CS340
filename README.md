# CS340
About the Project/Project Title
Grazioso Salvare is working with five animal shelters in Texas and will utilize this project. This “Animal Shelter Dashboard” project is designed to allow the user to look for dogs within the animal shelter’s database that fit their desired criteria to train them for search-and-rescue. Depending on the type of search-and-rescue needed, the user can categorize and identify potential candidates based on breed, age, etc. 


Motivation
A software application, like this one, is needed to provide Grazioso Salvare with a user-friendly, interactive, dashboard to identify dogs that could be used for search-and-rescue training. 


Getting Started
To get started, the user needs authorization. This includes a user and a password to access the database and utilize the CRUD operations and dashboard. I have created a username (accuser) and a password (Mulligan!23) option to grant this access. Once authorization is completed, they are allowed to access the dashboard and database.
To create this dashboard, I needed to include prior modules and files. I made sure to incorporate the CRUD capabilities and AnimalShelter file from a previous project. With this information, the user should have no issue maneuvering through the dataset to get what they need. The dashboard created includes multiple buttons (widgets) which allows the user to pinpoint different characteristics needed. The user can also access a pie chart and geolocation which displays usable data regarding their search(es). 


Installation
MongoDB and Jupyter Notebook were both used to execute this project efficiently. MongoDB allowed me to import the Animal Shelter data and create authorization for the users (from previous project). Jupyter Notebook allowed me to create the Python Modules necessary to create the CRUD functions necessary for the user. While starting out with Jupyter Notebook, it was imperative for me to call upon MongoDB so the previous data was applicable. Synergistically, these tools work great and will allow the user to interact with the dashboard in a way that will set their company up for success. 

Link for Grazioso Salvare Logo (used within dashboard): 
https://snhu.brightspace.com/content/enforced/851425-CS-340-T1036-OL-TRAD-UG.21EW1/course_documents/Grazioso%20Salvare%20Logo.png?_&d2lSessionVal=v3nq
5PFjNl8oFEi7JgDEVIGTI&ou=851425

The largest issue I faced while completing this project dealt with syntax and indentation. To overcome this obstacle, I constantly went back to edit and compile my code. Doing this periodically, would let me keep up with any potential errors I had. Ensuring all lines of code had the correct spacing and indentions was imperative for everything to cohesively run in the end.

Usage

Code Example
This portion of code is responsible for creating and displaying the widgets for the dashboard. This will allow the user to narrow down their searches and navigate to find desired data.
    className='row',
        style={'display': 'flex'},
        children=[
                html.Button(id='submit-button-one',n_clicks=0, children= 'Water Rescue'),
                html.Button(id='submit-button-two',n_clicks=0, children= 'Mountain or Wilderness Rescue'),
                html.Button(id='submit-button-three',n_clicks=0, children='Disaster Rescue or Individual Tracking'),
                html.Button(id='submit-button-four', n_clicks=0, children='Reset')          
        ]

Tests
Since multiple files are needed for this project to work properly, this portion of code reflects the test file needed to check the CRUD functionality and effectiveness of the animal_shelter file. All of these files work together to create the dashboard for the user. 
for i in animal_data:
  	  a.create(i)
dogs = a.read( {"type":"dog"}  )
for dog in dogs:
  	  print(dog)


 

Contact
Sarah Prince
