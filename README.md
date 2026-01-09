# PORTFOLIO PROJECT - HOLBERTON SCHOOL DIJON

This project is part the first year "Fundamentals" curriculum at Holberton School.

We were asked to imagine, design and develop a web application of our choice and to develop it.

This README describes **the different stages of my work** on this portfolio project, from `technical documentation` to code.

## INTRODUCTION :
### Purpose of the application:
This application offers an open-source solution for cultural organisations to manage their bookings.
### Problem statement:
Cultural organisations such as local museums and associations need sometimes some open-source or free-to-use solutions for economic reasons : they use several tools to manage their booking, analyze their audiences, generate invoices...

This application aims to bring together three main features : 
- booking scheduling, 
- automatic document generation based on scheduling informations (contracts, invoices...),
- data extraction for reporting purpose,

## TECHNICAL DOCUMENTATION
### USERS STORIES
**As a user...**
I want to create booking an register client informations

### MOCKUPS

### SYSTEM ARCHITECTURE AND TECHNOLOGY STACK
<details><summary> Display section details</summary>

<img src="./Documentation_files/portfolio_architecture.jpg"></img>

This application follow a monolithic application three-tiers client-server logic architecture :
- <u>presentation layer</u> : a `front-end` interface allowing users to log in and create, update and view bookings;
- <u>business logic</u> : a `back-end` exposing a RESTful API that receive user queries from the front-end and apply business rules;
- <u>data an persistence layer</u> : a `relational database` used to store bookings, structures, booking types, users, etc.;


#### Technology stack : 
-  <u>Front-end</u> : <br>
**HTML5, CSS3, JavaScript**<br>
Interface is built with `HTML5`, `CSS3` and `JavaScript` for interactivity and `client-side rendering`.<br>
Users access to data via HTTP requests through a RESTful API.

- <u>Back-end</u> :<br>
**Facade pattern, python, Flask RESTX API, ORM SQLAlchemy**<br>
Back-end is responsible of `business logic`.<br>
It exposes a `RESTful API` that receives user requests and returns data.<br>
A `Facade pattern` is used to process requests :  it orchestrates object creation and data storage making the code easier to maintain and update.<br>
`SQLAlchemy` will allow to manipulate data as objects, making requests safer and to focus on object-oriented paradigm.

- <u>Database</u> :<br>
**MySQL**<br>
Entities have strong relationships, that is why an SQL database is chosen.<br>
`SQLAlchemy ORM` is used by the back end to define models, manage database schema and perform queries.<br>
Since there is no need of extensibility, specific data types and no advanced features, `MySQL` is well suited for the project's requirements : easy to maintain, open-source, well documented, and well known by the developer team. 
</details>

### COMPONENTS - CLASS DIAGRAM
### ENTITIES RELATIONSHIP DIAGRAM
### SEQUENCES DIAGRAMS
### INTERNAL API DOCUMENTATION
