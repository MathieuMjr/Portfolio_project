# UPDATE INCOMING SOON
Your are currently reading the technical documentation written during the preparatory work. 
An actual technical documentation is coming.

# PORTFOLIO PROJECT - HOLBERTON SCHOOL DIJON

This project is part the first-year "Fundamentals" curriculum at Holberton School.

The goal is to imagine, design and develop a web application of our choice in three months.

This README describes the final documentation of my project.

## INTRODUCTION :
### Purpose of the application:
This application offers an open-source solution for cultural organisations to manage their reservations.
The solutions proposed by my web app are strongly linked to my previous experience as employee of scientific culture association.
### Problem statement:
Cultural organisations such as local museums and associations need sometimes some open-source or free-to-use solutions for economic reasons : they use several tools to manage their reservations, analyze their audiences, generate invoices and agreements...

This application aims to bring together three main features : 
- reservation scheduling, 
- automatic document generation based on scheduling information (contracts, invoices...),
- data extraction for reporting purpose,

## TECHNICAL DOCUMENTATION
### USERS STORIES
<details> <summary>Show users stories</summary>
This section presents the users stories, so that we can imagine the app and define requirements from a user perspective : what they aim to achieve and what are their.

#### As a user I want to...

- `create a reservation` so that I can manage my planning<br>*`Must have`*

- `register client's contact` information so that I can keep in contact with them all along the reservation process.<br>*`Must have`*

- `register the activity information` (theme, price, audience) requested by the client, so that I can prepare the activity (animation, exhibition visit, etc.).<br>*`Must have`*

- use reservation information to `generate an agreement`, so that I can formalize the reservation.<br>*`Should have`*

- use reservation information to `generate a recap` for the client, so that the client and I have the same information of the reservation.<br>*`Should have`*

- use reservation information to `generate an invoice`, so that I can be paid by the client after the service has been delivered. <br>*`Should have`*

- `track the reservation status`, so that I can know which work still needs to be done.<br>*`Could have`*

- `extract my reservations` in a csv file so that I can analyze my audiences and my general activity.<br> *`Should have`*

#### As a manager, I want to...
- `Create and manage users` so my employees can loggin the application and create their reservations<br> *`Must have`*

- `view every reservation` of all users so I can have an overview of the activity.<br> *`Should have`*

- be able to `extract all the reservations` so I can produce an activity report for the organisation.<br> *`Should have`*

- `access every reservation : creation and update` so I can take action in case a collaborator is unavailable.<br> *`Should have`*
</details>

### MOCKUPS
<details><summary>Show Mockups section</summary>
On the basis of users stories, this section provide three statics mock ups, illustrating the user's journey on the application from login to the screen of reservation creation.

A sober style is intentionally chosen to make the application easy to use. 

**Login screen**
<img src='./documentation_files/overview_login_screen.png'></img>

Users use their mail and password to authenticate. It's the first screen every user encounters.

**Planning screen**
<img src='./documentation_files/overview_planning_screen.png'><img>

After login, users land on this page.<br>
They can see essential reservation details for each days, and access a reservation details by a simple click on the wanted reservation's card.

<u>UI evolutions</u> :
- First card should be a monday and last card a sunday
- May be a row for each day will be prefered if it is too hard to display by cards
- The name of the day should be displayed
- Some filters could sort reservations by status or reservation types.

**Reservation creation screen**
<img src='./documentation_files/initial_design/overview_reservation_screen.png'><img>
<img src="./documentation_files/initial_design/overview_reservation_screen_bis.png"></img>

The screen display a form with all fields needed to create a reservation.

After defining the structure type and the ZIP code of the beneficiary structure, a list of existing structure in the database is populated.<br>
Once the wanted structure is selected, the adress, phone and email fields are populated.

The same form is displayed when an existing reservation is accessed. 
Then, the input fields are populated with data of the existing reservation and can be updated.

<u>UI Evolution</u> :
- An icone to create structures should be displayed
</details>

### SYSTEM ARCHITECTURE AND TECHNOLOGY STACK
<details><summary> Show architecture and technology section</summary>

<img src="./documentation_files/initial_design/portfolio_architecture.jpg"></img>

This application follow a monolithic application three-tiers logic client-server architecture :
- <u>presentation layer</u> : a `front-end` interface allowing users to log in and create, update and view reservations;
- <u>business logic</u> : a `back-end` exposing a RESTful API that receive user queries from the front-end and apply business rules;
- <u>data and persistence layer</u> : a `relational database` used to store reservations, structures, reservation types, users, etc.;


#### Technology stack : 
-  <u>Front-end</u> : <br>
**HTML5, CSS3, JavaScript**<br>
Interface is built with `HTML5`, `CSS3` and `JavaScript` for interactivity and `client-side rendering`.<br>
Users access to data via HTTP requests through a RESTful API.

- <u>Back-end</u> :<br>
**Services layer, Python, Flask RESTX API, ORM SQLAlchemy**<br>
Back-end is responsible for `business logic`.<br>
It exposes a `RESTful API` that receives client requests and returns structured data.<br>
`Pydantic` validates values and types in payload received from the API when resources are created or updated.<br>
`Services` classes are responsible for applying business rules before persisting data<br>
`SQLAlchemy` allows data manipulation through Python objects, improving safety, readability, and adherence to the object-oriented paradigm.

- <u>Database</u> :<br>
**SQLite**<br>
The application relies on a relational database du to strong relationships between entities.<br>
`SQLAlchemy ORM` is used by the back end to define models, manage database schema and perform queries.<br>
For the MVP, an `SQLite` database is choosen ; this choice is well suited to the project's requirements: no need for horizontal scalability, no advanced data types or database-specific features, easy setup and maintenance, open-source and well documented.<br>
In a second instance, a more robust database systeme such as MySQL can be implemented.
</details>

### ENTITIES RELATIONSHIP DIAGRAM
<details><summary>Show entities relationship section</summary>

Based on user needs identified in the user stories, this section present the entities, relationships and explains key design choices of the model.

Since storing data on reservations is a the core of the application, the ER diagram was designed first.

#### <u>Diagram</u> :
This diagram picture the general structure of the database tables and, attribute types, primary and foreign keys and relationships. 

[<img src='./documentation_files/er_diagram.png'></img>]()
[Access to full view](https://www.mermaidchart.com/d/88b7aaa7-8f0f-4790-bf29-e7feb92990aa)<br>
[Access to Mermaid code](./documentation_files/er_diagram_code.txt)

The reservation entity is central in the ER diagram and almost all its attributes are related to other entities. 

In order to understand the relationships between reservation and other entities, some clarifications might be needed on modeling decisions.

#### <u>Modeling decisions</u>:
The following points explain specific modeling decisions :

**Attributes**
- `users role`<br> User can be a manager or not.<br> A manager have access to specific CRUD operations (see [Internal API Documentation](#routes-and-authorizations-)).

- `reservation attributes "contact"`<br> Is not the structure contact but the contact of the specific person, from the structure, in charge of the reservation. <br>Sometimes, the contact from the structure is not the same person from a reservation to another. <br>Then, the contact is specific to the reservation.

**Relationships**
- `relationship users/reservation_types`<br> User can't create any type of reservation.<br> A list of reservation_types tels which type of reservation a user can manipulate.<br> Someone in charge of animation can't create reservation for an exhibition rental.

- `relationship themes/reservation_types` <br> Each kind of reservation_types have a specific list of themes.

**Entities**
- `reservation_types`<br> Are referring to the kind of activity booked : exhibition visit, outdoor animation, etc.

- `audiences_types, themes, reservation_types, structures_types`<br> Are needed to keep data consistency and integrity.<br> Types can be useful for reports. Having types entities avoids having the same value written in different ways.


#### <u>Relationships with reservation entity</u>:

Let's take a look at relationships with reservation entity.

Table | Relationship with reservation | Commentary
--|--|--|
USERS | 1-N | A reservation is authored by one user<br> A user can author zero or many reservations
STRUCTURES | 1-N | A reservation has one structure<br> A structure can do many reservations
RESERVATION_TYPES | 1-N | The structure must book one activity<br> An activity can be booked many times
THEMES | N-N | A structure can book many themes <br> A theme can be booked many times
AUDIENCES | 1-N | A reservation have several audiences ; and audience is a school level and a count of school children<br> An audience is unique to a reservation. 
STATUS | 1-N | A reservation got only one status, indicating at which step the reservation is<br> Many reservation use the same statuses.

</details>

### COMPONENTS - CLASS DIAGRAM
<details><summary>Show Class diagram section</summary>
This section presents the classes and methods of our business logic layer.\
The use of SQLAchemy ORM helped to transform tables (except join tables) from ER diagram into classes. 

<img src='./documentation_files/class_diagram.png'></img>
[Access to Mermaid JS Code](./documentation_files/class_diagram.txt)

#### Modeling choices

**Base class**

The base class is an abstract class that all objects inherit from. It give them an auto-generated UUID and a creation date (timestamp). 

In addition, a boolean attribute "is_active" is *defined, since data deletion won't be authorized to keep integrity and historical consistency to our database. 

**Facade class**

Using the facade pattern, a facade class will provide methods for object manipulation : creation, storage, update, etc. 

This provide better maintainability of the codebase. 

**Repository class**

Ultimately, several repository classes will be implemented, inheriting from an abstract Repository class that defines core methods for objects. 

Child repository classes might define specific methods once SQAlchemy is implemented, allowing fine grained request by specific attributes. 

 
</details>

### SEQUENCES DIAGRAMS<br>

<details><summary> Show sequences diagram section</summary>

hree high-level sequence diagrams illustrate the communication between each layer detailed in the previous section.
<br><br>

**Login**
<img src='./documentation_files/auth_sequence_diagram.png'></img>
[Access Mermaid JS code](./documentation_files/auth_sequence_diagram.txt)

Users send credentials to the API. An access token is generated if authentication succeeds, otherwise, an error message is returned. 

**Reservations view / Landing page loading**

<img src='./documentation_files/display_reservation_sequence_diagram.png'></img>

[Access Mermaid JS code](./documentation_files/reservation_display_sequence_diagram.txt)

After the user logs in, the landing page is loaded and fetches the API to retrieve reservations for the current month.\
The token identity is checked and only the reservations a user has authored are displayed.\
If the user is a manager, every reservation for the current month are displayed. 

**Reservation creation**
<img src='./documentation_files/reservation_creation_seq_diagram.png'></img>
[Access Mermaid JS code](./documentation_files/reservation_creation_seq_diagram.txt) 

When a user creates a reservation, the token identity is checked to determine if he has required authorizations to create a reservation for the selected reservation type.<br>
Data input is validated and if everything is correct, the resource is created.
</details>

### INTERNAL API DOCUMENTATION
<details><summary>Show API Documentation section</summary>
This section explain the application API rules, the routes and methods allowed, the status codes and the input and output formats for the main classes.

#### <u>Methods rules </u>:
- **POST** <br> Allows resource creation, a data input is required;
- **GET**<br> Allows resource retrieval.<br> A specific resource can be retrieved if route allow `path parameter` - otherwise, all resources are retrieved;
- **PUT** <br>Allows resource update ; a data input is required and `path parameter` is necessary to specify which resource to update;
- **DELETE** <br>
`Delete methods are not allowed` to keep data integrity and historical consistency.<br> Instead, resources will be marked as `inactive`;

#### <u>Routes and authorizations</u> :
**Users** can create `reservations` and `themes` in reservation types they are allowed to.<br>
They can create, update and retrieve `structures`.<br>
They can `access reservations` they authored. <br>
They can create and modify `audiences` to their reservations.

**Manager** can `access all resources`.<br>
They are the only ones that can perform `types` (reservation, audience, structure) and `status` creation and update. 

`Some routes might need to be refactored, as certain resources can be better represented as sub-resources.`

Route | Methods allowed | Path parameter | Authorizations | Action
|--|--|--|--|--|
`/login` | **POST** | / | - No authorizations needed | Gives access token to user if authentication success
`/user` | **POST**<br>**PUT**<br>**GET** |  user_id | - Manager role required | User(s) management
`/reservations` | **POST**<br>**PUT**<br>**GET** | reservation_id | - Reservation type authorization required<br> -Author authorization<br>- Manager role | Manage reservations
`/reservation_types` | **POST**<br>**PUT**<br>**GET** | type_id | - Manager role for POST and PUT<br> - Authentication for GET | Manager reservation types
`/structures` | **POST**<br>**PUT**<br>**GET** | structure_id<br> | - Authentication needed | Manage structres
`/structure_types` | **POST**<br>**PUT**<br>**GET** | structure_id | - Manager role for POST and PUT<br> - Authentication for GET | Manage structure types
`/themes` | **POST**<br>**PUT**<br>**GET** | theme_id | - Reservation type authorization<br> - Manager role | Manage themes
`/audience` | **POST**<br>**PUT**<br>**GET** | reservation_id ? | - Reservation's author authorization<br> - Manager role | Manage audiences
`/audience_types` | **POST**<br>**PUT**<br>**GET** | type_id | - Manager role for POST and PUT<br> - Authentication for GET | Manage audience types

#### <u>Data input and output format</u> :

Input and output data is in `JSON` format.<br>

To perform **POST** and **PUT** request, you can refer to the attribute shown in the [`class diagram`](#components---class-diagram). 

#### <u>Status codes and messages</u>:

Status code | Message | Meaning |
|--|--|--|
200 | OK | Resource successfully retrieved<br> `GET method` | 
201 | Created | Resource successfully created<br> `POST method`|
400 | Invalid input | Some data in the input are not in the expected format<br> `POST method`
401 | Invalid credentials | Wrong credentials registered while logging in<br> `POST method` *on login route* 
403 | Unauthorized action | User tried to access a route he is not allowed to 
404 | Resource not found | User tried to access a specific resource, but it can't be found<br> `PUT method`<br> `GET method`
</details>

### SCM AND QA PLAN

<details><summary>Show SCM and QA plan section</summary>
This section details the modus operandi for versioning strategy and testing.<br><br>

**SCM strategy**

`Git` will be use for code version control. 

`GitHub` will be used as a remote repository, making sure the latest version of code is available on the cloud.

Three branches will be used :
- <u>Production branch</u><br>
This branch will contain stable and tested code, ensuring that a working version is always available.
- <u>Development branch</u><br>
This branch will be used to develop new features without breaking the production version.
- <u>Test branch</u><br>
This branch will be used to test the code from development branch before merging it into the production branch. 

**Commit and merging strategy**

A commit is made in development branch whenever a feature is developed and seems functional.<br>
A verb will explain what action has been done : "added new function for...", "fixed return and status code", "configured database", etc.

<u>Merges occurs in the following order</u> :<br> dev branch --> test branch -- *if success* --> production branch -- *new feature* --> dev branch<br>
dev branch --> test branch -- *if fails* --> dev branch

**QA strategy**

Several tests will be performed according to the stage of development before any merge into the production branch.

- <u>Object creation</u> :<br>
Unit tests will check if objects are well created with the expected attribute values.<br>
Tests should verify that  expected errors are thrown in case of wrong data type for exemple. 
- <u>API methods and response</u> :<br>
Postman will be used to test routes and methods.<br> IDs and tokens will be stored in environment variables.<br>
Some failing tests will be implemented to verify expected status codes and response messages.
- <u>SQLAlchemy ORM</u> :<br>
When the project has transitioned from in memory repository to database repository, tests from Postman should still be functional and should give the same results.

</details>

