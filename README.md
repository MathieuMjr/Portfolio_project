# PORTFOLIO PROJECT - HOLBERTON SCHOOL DIJON

This project is part the first-year "Fundamentals" curriculum at Holberton School.

We were asked to imagine, design and develop a web application of our choice.

This README describes **the different stages of my work** on this portfolio project, from `technical documentation` to code.
## NAVIGATION :
- [Introduction](#introduction-)
- [Technical documentation](#technical-documentation)
    - [Users stories](#users-stories)
    - [Mockups](#mockups)
    - [System architecture and technology stack](#system-architecture-and-technology-stack)
    - [Entities relationship diagram](#entities-relationship-diagram)
    - [Components - class diagram](#components---class-diagram)
    - [Sequences diagrams](#sequences-diagrams)
    - [Internal API documentation](#internal-api-documentation)
        - [Methods rules](#methods-rules-)
        - [Routes and authorizations](#routes-and-authorizations-)
        - [Data input and output format](#data-input-and-output-format-)
        - [Status code and messages](#status-codes-and-messages)
## INTRODUCTION :
### Purpose of the application:
This application offers an open-source solution for cultural organisations to manage their bookings.
### Problem statement:
Cultural organisations such as local museums and associations need sometimes some open-source or free-to-use solutions for economic reasons : they use several tools to manage their booking, analyze their audiences, generate invoices...

This application aims to bring together three main features : 
- booking scheduling, 
- automatic document generation based on scheduling information (contracts, invoices...),
- data extraction for reporting purpose,

## TECHNICAL DOCUMENTATION
### USERS STORIES
This section presents users stories so that we can imagine the app and define requirements from a user perspective.
<details> <summary>Display users stories</summary>

Users stories describe what users can do within the application, and what they aim to achieve. They help understand their needs and  will guide the following steps in designing the application.

#### As a user I want to...

- `create a booking` so that I can manage my activity

- `register client's contact` information so that I can keep in contact with them all along the booking process.

- `register the activity information` (theme, price, audience) requested by the client, so that I can prepare the activity (animation, exhibition visit, etc.).

- use booking information to `generate an agreement`, so that I can formalize the booking.

- use booking information to `generate a recap` for the client, so that the client and I have the same information of the booking.

- use booking information to `generate an invoice`, so that I can be paid by the client after the service has been delivered. 

- `track the booking status`, so that I can know which work still needs to be done.

- `extract my bookings` in a csv file so that I can analyze my audiences and my general activity. 

#### As a manager, I want to...
- `view every booking` of all users so I can have an overview of the activity.

- be able to `extract all the bookings` so I can produce an activity report for the organisation.

- `access every booking : creation and update` so I can take action in case a collaborator is unavailable.
</details>

### MOCKUPS
This section provide few mockups to illustrate some main users stories.

Now we know what users and managers want to do and why, let's put those stories in pictures with mockups to get an overview of the user experience. 

### SYSTEM ARCHITECTURE AND TECHNOLOGY STACK
<details><summary> Display architecture and technology details</summary>

<img src="./Documentation_files/portfolio_architecture.jpg"></img>

This application follow a monolithic application three-tiers logic client-server architecture :
- <u>presentation layer</u> : a `front-end` interface allowing users to log in and create, update and view bookings;
- <u>business logic</u> : a `back-end` exposing a RESTful API that receive user queries from the front-end and apply business rules;
- <u>data and persistence layer</u> : a `relational database` used to store bookings, structures, booking types, users, etc.;


#### Technology stack : 
-  <u>Front-end</u> : <br>
**HTML5, CSS3, JavaScript**<br>
Interface is built with `HTML5`, `CSS3` and `JavaScript` for interactivity and `client-side rendering`.<br>
Users access to data via HTTP requests through a RESTful API.

- <u>Back-end</u> :<br>
**Facade pattern, python, Flask RESTX API, ORM SQLAlchemy**<br>
Back-end is responsible for `business logic`.<br>
It exposes a `RESTful API` that receives user requests and returns data.<br>
A `Facade pattern` is used to process requests :  it orchestrates object creation and data storage making the code easier to maintain and update.<br>
`SQLAlchemy` will allow to manipulate data as objects, making requests safer and to focus on object-oriented paradigm.

- <u>Database</u> :<br>
**MySQL**<br>
Entities have strong relationships, that is why an SQL database is chosen.<br>
`SQLAlchemy ORM` is used by the back end to define models, manage database schema and perform queries.<br>
Since there is no need of extensibility, specific data types and no advanced features, `MySQL` is well suited for the project's requirements : easy to maintain, open-source, well documented, and well known by the developer team. 
</details>

### ENTITIES RELATIONSHIP DIAGRAM
Since this application is about storing data on bookings, ER diagram was the first designed. 

The following diagram shows the different entities of our booking system and their relationships.

The following diagram was creating using Mermaid.js. 

`Click on the picture` to get a full view of the diagram or copy the following code in [Mermaid.js](https://mermaid.live/).
<details>
<summary> Show Mermaid.js code</summary>

```
erDiagram
    USERS {
        varchar id(PK)
        varchar first_name
        varchar last_name
        varchar password
        varchar email
        varchar role
    }
    RESERVATIONS {
        varchar id(PK)
        varchar date
        varchar structure_id(FK)
        varchar author_id(FK)
        varchar type_id(FK)
        varchar status_id(FK)
        float price
        varchar contact_first_name
        varchar contact_last_name
        varchar contact_role
        varchar contact_email
        varchar contact_phone
    }
    STATUS {
        varchar id(PK)
        varchar name
    }
    AUDIENCES {
        varchar id(PK)
        varchar reservation_id(FK)
        varchar audience_type_id(FK)
        int count
    }
    AUDIENCE_TYPES {
        varchar id(PK)
        varchar name
    }
    STRUCTURES {
        varchar id(PK)
        varchar name
        varchar adress
        varchar zip_code
        varchar town
        varchar email
        varchar phone
        varchar structure_type_id
    }
    STRUCTURE_TYPES {
        varchar id(PK)
        string name
        bool is_school
    }
    RESERVATION_TYPES{
        string id(PK)
        string name
    }
    THEMES {
        string id(PK)
        string reservation_type_id(FK)
        string name
    }
    RESERVATION_THEMES {
        string reservations_id(FK)
        string theme_id(FK)
    }
    RESERVATIONS }o--|| RESERVATION_TYPES : has
    THEMES ||--|{ RESERVATION_THEMES : part_of
    RESERVATIONS ||--|{ RESERVATION_THEMES : has
    RESERVATION_TYPES ||--|{ THEMES : has
    USERS ||--o{ RESERVATIONS : makes
    STATUS ||--|{ RESERVATIONS : has
    RESERVATIONS }o--|| STRUCTURES : has
    STRUCTURES }o--|| STRUCTURE_TYPES : has
    AUDIENCES ||--|{ AUDIENCE_TYPES : has
    RESERVATIONS ||--o{ AUDIENCES : has
```

</details>

[<img src='./Documentation_files/er_diagram.png'></img>](https://www.mermaidchart.com/d/88b7aaa7-8f0f-4790-bf29-e7feb92990aa)

Bookings are at the core of our structure. 

Attributes `highlighted` are referring to entities (tables) linked to the booking.


A booking is : 
- authored by one `user` ; users can create several bookings
- for a `structure` ; a structure can have many reservations
- refering to a specific activity (reservation_type) such as animation, exhibition visit, or exhibition rent ; many bookings can share the same reservation_type.
- having some `themes`, according to the `reservation_type` ; themes can be shared by many reservations
- have many `audiences` from the structures details by their school level ; an audience is unique to a reservation
- have contact information ; this contact is not linked to the structures since teachers booking can change from a booking to another.
- a price
- one `status` indicating at which step the booking is ; status are shared by many reservations


For **consistency reasons**, some `types` have been created for `reservations`, `structures` and `audiences`. Users will use types instead of writing it on their own, which could result in types written in different ways. 


### COMPONENTS - CLASS DIAGRAM


### SEQUENCES DIAGRAMS

### INTERNAL API DOCUMENTATION

This section explain the application API rules, the routes and methods allowed, the status codes and the input and output formats for the main classes.
<details><summary>Show API Documentation</summary>


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



