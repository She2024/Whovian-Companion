
# R1 Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

While it’s easy to locate a list of episodes by Dr regeneration or actor, there is no easy way to search and locate an episode of Dr Who by an enemy. Sometimes you just really want to watch a particular villain get put in their place by your favourite alien hero.

This web app will let you search a library of DR Who episodes, for all the episodes your chosen enemy of the Dr appears in. You will also be able to search by Dr using the the actors name or the Dr regeneration. This can be handy if you remember the actors name but can’t remember where that actors iteration of the Dr sits in the whovian histories and vice versa. For added convivence, the user can create a list of the episodes they currently own to create their own library list. This would allow the user to search for the episode they want to watch and check if they currently own it.


# R2 Describe the way tasks are allocated and tracked in your project.

The use of Trello https://trello.com/b/mOpl00Gq/t2a2-api-webserver and Github https://github.com/She2024/Whovian-Companion

Trello cards show task to be completed and remind me of the current progress level. Cards are moved between task headings like, Planning, To-Do , Doing and Done, to show progress and curret status. 
Git hub is used for version control and when compared to the trello board shows me where I'm up to. 


# R3 List and explain the third-party services, packages and dependencies used in this app.
    
    bcrypt==4.2.0 - for password encryption
    Flask==3.0.3 - to run app
    Flask-Bcrypt==1.0.1 to allow flask and Bcrypt to understand each other    
    Flask-JWT-Extended==4.6.0 - to create a JWT token to be saved in the users device to make future login easier
    flask-marshmallow==1.2.1 - to allow flask and marshmallow to understand each other     
    Flask-SQLAlchemy==3.1.1 - to allow flask and SQL to understand each other    
    marshmallow==3.22.0 - it's an Object Relational Management framework to validate data, deserialise and serialise objects in python. 
    marshmallow-sqlalchemy==1.1.0 - to allow marshmallow and SQL to understand each other    
    psycopg2-binary==2.9.9 - supports secure connection between python and postgresql   
    python-dotenv==1.0.1 - to support the vertual environment
    SQLAlchemy==2.0.35 - the Database 
    

# R4 Explain the benefits and drawbacks of this app’s underlying database system.

Postgresql is scaleable, versitle and supports many languages. Complex to set up.

# R5 Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.
Authorisation - confirm data is true - confirm is user registered, are login details correct, does library exist
User - stores user details and is user is admin
Library - stores details of episodes entered by user

# R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.

See ERD diagram version 4 saved in documents sub-folder under the src folder for the API. 

Build planed for a database the user could store a list of the episodes they own. User can access a large database of all episodes released related via a joining table with the User ID and the Epidsode number. 

# R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation.

This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

# R8 Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:

HTTP verb
 GET - fetch a specific library - used to retrieve regislation, login or details saved to the library. 
 POST - create a new library - user enteres detials 
 DELETE - delete a library - user can delete their own entries as needed
 PUT, PATCH - edit a library entry, update user details

Path or route
Routes to reduce reduncy in coding using blueprint

Any required body or header data

Response

