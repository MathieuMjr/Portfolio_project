# UPDATE IN PROGRESS - 2026 - 04 - 02

# PORTFOLIO PROJECT - HOLBERTON SCHOOL DIJON

During my Fundamentals curriculum at Holberton School, I was asked to imagin, design and develop a web application as a end-of-the-year project.

Now that I successfully passed my demo, I continue to make Kō.tools evolve !

## INTRODUCTION :

### Licence:
Kō.tools is under Creative Commons licence CC-BY-SA-NC :
- BY : it is free to use but must you credit my work
- SA : you can reuse and modify it if the modified product is under the same licence
- NC : you can't use or modify Kō.tools for commercial purpose without my consent

### Purpose of the application:
On the basis of my experience as workshop facilitator in an assocation promoting scientific literacy, I imagined Kō.tools as a self-hosted web application to help cultural organizations into their reservation management.

The end objective is to create a flexible solution with : 
- customizable users protected access for employees to manage their own planning
- customizable reservation types according to the organization activities
- customizable audience types
- customizable structure types
- etc.

### Problem statement:
Cultural organisations such as local museums and associations need sometimes free and easy to use solutions : they use several tools to manage their reservations, analyze their audiences, generate invoices and agreements... multiplying the information inputs.

This application aims to bring together three main features : 
- reservation scheduling, 
- automatic document generation based on scheduling information (contracts, invoices...),
- data extraction for reporting purpose,

## APPLICATION DESIGN

**An actual an updated state of work about the application design is in progress.**

<details><summary>Initial preparatory work</summary>

You can take a look at the preparatory work on Kō.tools made during for Holberton School purpose in the directory [`documentation_files`](./documentation_files/inital_design) with the following information : 
- users stories
- mockups
- system architecture and technology stack
- entity relationship diagram
- class diagram
- sequences diagrams
- API planning
- SCM and QA plan
</details>

## WORK IN PROGRESS
**Short term:**
- Security improvement : sensible data encryption, front-end field validation, stronger back-end field validation to avoid injection, server-side cookie generation for token.
- Front-end : admin dashboard with access to catalog entities management, structure creation from reservation form screen.
- Back-end : required information policy for entities so it make sense to use the reservation status "waiting for more information", rework pydantic schemas with stronger on values validations.
- Deployement : create docker containers
- Tests : implement integration test for services
<br>

**Mid/long term:**
- Implement templated based document generation
- Implement data export
- Finest role management with read only accesses

## STACK, TECHNOS, ARCHITECTURE, DOCUMENTATION
**Files overview**
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── audience_types.py
│   │   ├── login.py
│   │   ├── res_types.py
│   │   ├── reservations.py
│   │   ├── statuses.py
│   │   ├── struct_types.py
│   │   ├── structures.py
│   │   └── users.py
│   ├── extensions.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── audience.py
│   │   ├── audience_type.py
│   │   ├── base.py
│   │   ├── reservation.py
│   │   ├── reservation_type.py
│   │   ├── status.py
│   │   ├── structure.py
│   │   ├── structure_type.py
│   │   ├── theme.py
│   │   └── user.py
│   ├── persistence
│   │   ├── __init__.py
│   │   ├── audience_repository.py
│   │   ├── audience_type_repository.py
│   │   ├── repository.py
│   │   ├── reservation_repository.py
│   │   ├── reservation_type_repository.py
│   │   ├── status_repository.py
│   │   ├── structure_repository.py
│   │   ├── structure_type_repository.py
│   │   ├── theme_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── code_snippet
│   │   ├── errors.py
│   │   ├── notes
│   │   ├── reservation_service.py
│   │   ├── structure_service.py
│   │   ├── user_service.py
│   │   └── utils.py
│   └── validators
│       ├── __init__.py
│       ├── audience.py
│       ├── audience_type.py
│       ├── reservation.py
│       ├── reservation_type.py
│       ├── status.py
│       ├── structure.py
│       ├── structure_type.py
│       ├── theme.py
│       └── users.py
├── config.py
├── conftest.py
├── documentation_files
│   ├── Stage 5 report.pdf
│   ├── er_diagram_code.txt
│   ├── initial_design
│   │   ├── README.md
│   │   ├── auth_sequence_diagram.png
│   │   ├── auth_sequence_diagram.txt
│   │   ├── class_diagram.png
│   │   ├── class_diagram.txt
│   │   ├── display_reservation_sequence_diagram.png
│   │   ├── er_diagram.png
│   │   ├── er_diagram_code.txt
│   │   ├── overview_login_screen.png
│   │   ├── overview_planning_screen.png
│   │   ├── overview_reservation_screen.png
│   │   ├── overview_reservation_screen_bis.png
│   │   ├── portfolio_architecture.jpg
│   │   ├── reservation_creation_seq_diagram.png
│   │   ├── reservation_creation_seq_diagram.txt
│   │   └── reservation_display_sequence_diagram.txt
│   └── stage 4 report.pdf
├── eslint.config.mjs
├── exports
│   └── env.json
├── front
│   ├── css
│   │   ├── backup_css
│   │   │   ├── login.css
│   │   │   ├── planning.css
│   │   │   └── reservation.css
│   │   ├── login.css
│   │   ├── planning.css
│   │   └── reservation.css
│   ├── html
│   │   ├── header.html
│   │   ├── index.html
│   │   ├── planning.html
│   │   ├── planning_nav.html
│   │   └── reservation.html
│   ├── js
│   │   ├── api.js
│   │   ├── auth.js
│   │   ├── config.js
│   │   ├── header.js
│   │   ├── index.js
│   │   ├── planning.js
│   │   ├── reservation backup.js
│   │   ├── reservation.js
│   │   ├── reservation_ui.js
│   │   └── utils.js
│   └── medias
│       ├── add-icon.png
│       ├── arrow_left.png
│       ├── arrow_right.png
│       ├── calendar.png
│       ├── import-icon.png
│       ├── koto logo-01-01.png
│       └── power.png
├── instance
│   └── test.db
├── package-lock.json
├── package.json
├── requirements.txt
├── run.py
├── seed
│   ├── __init__.py
│   ├── seed_admin.py
│   ├── seed_audience_types.py
│   ├── seed_db.py
│   ├── seed_res_types_theme.py
│   ├── seed_status.py
│   └── seed_struct_types.py
└── tests
    ├── postman
    │   └── Ko.tools.postman_collection.json
    ├── seeds
    │   ├── __init__.py
    │   ├── seed_admin.py
    │   ├── seed_audience_types.py
    │   ├── seed_db.py
    │   ├── seed_res_types_theme.py
    │   ├── seed_status.py
    │   └── seed_struct_types.py
    ├── test_audience.py
    ├── test_audience_type.py
    ├── test_base.py
    ├── test_reservation.py
    ├── test_reservation_type.py
    ├── test_status.py
    ├── test_structure.py
    ├── test_structure_type.py
    ├── test_theme.py
    └── test_users.py

21 directories, 133 files
```

Main directory | Subdirectory | Responsibility
|--|--|--|
/app | /api | Defines API namespaces, routes and allowed methods with token verifications to manage access control.
/app | /models | SQL Alchemy models<br><br> `base.py` is the abstract class all object inherit from.
/app | /persistence | Repositories that manage database interaction.
/app | /services | Services are called by the API layer and enforce business logic.
/app | /validators | Pydantic schemas called by the service to validate payloads and data
/docs | - | Landing page prototype asked by Holberton School - about to be deleted
/documentation_files | - | Contains reports and initial documentation asked by Holberton School
/exports | - | Contains file generated by seed execution with all object name and ids in the database ready to be imported in Postman
/front | /css<br>/html<br>/js | Files in charge of presentation layer
/seed | - | Admin and catalog values creations to populate database.<br> Temporary until routes are created for catalog values.
/tests | ./ | Pytests that checks for objects instanciation and persistence
/tests | /postman | Contains exportable json of Postman requests collection
/tests | /seeds | Special seeds for test with deactivated values
/Portfolio_project | - | `config.py` define test, debug and classic configuration for the app factory. <br> `conftest.py` define configuration and fixtures for pytest.<br> `requirements.txt` contains version information on technologies.<br>`run.py` file to run to start the app.

**Architecture and technos**<br>
Ko.tools uses a three layer architecture : 
- Presentation layer in charge of client rendering.
- Application layer in charge of requests, business logic and database interactions.
- Persistence layer in charge of the database.
<br>
<br>
Front-end | Back-end | Database
|--|--|--|
HTML 5<br> CSS3<br> Vanilla JavaScript | Python 3<br> Flask<br> Flask RestX <br> Flask JWT extended <br> Flask BCrypt<br> Pydantic<br>Dotenv | SQL Alchemy<br> MySQL <br> SQLite (for tests)

**ER Diagram**<br>
The following Entity-Relationship diagram explain you the main entity of the web application.

To sum up quickly :
- Four main entities : users, structures, reservations and audiences
- Five catalog entities to ensure data consistency : audience types, reservation types, structure types, statuses, themes.

<br>

*- Soft delete policy -*<br>
A soft delete policy has been defined : entities cannot be hard deleted to avoid history loss :
- All entity have a "is_active" field.
- Reservations are not "deactivated" but has a "cancelled" status instead.
- Deactivated entities cannot be retrieved unless accessed from the admin dashboard.
- Deactivated entities retrieval will raise a 404 error.

<br>

**API Documentation**

To access API documentation : 
- run the application
- access http://localhost:5000/api

Please, notice that for now, parameters are missing and will be updated next. (Focused on Pydantic validation instead of Swagger validation).

<details><summary>Users</summary>

Method | Route | Parameters | Body | Code responses | Example response | Privilèges requis ?
--|--|--|--|--|--|--|
**GET** | /api/users/ | / | / |200 - Success<br> | {<br>"id": string,<br>"firstname": string,<br>"email": string,<br>"role": boolean,<br>"reservation_types":[strings],<br>"is_active": boolean<br>}
**POST**| /api/users/ | / | {<br>""} | 201 Created<br>400 Invalid input<br>404 Resource not found<br> 409 Unique Constraint Violation | {<br>}
**GET** | /api/me | / | / | 200 Sucess | A remplir
**PUT** | /api/me | / | A remplir | 200 Success<br> Ajouter échec d'inputs | A remplir
**GET** | /api/users/ | user_id | / | 200 OK<br> 403 Priviledge required <br> 404 Ressource not found | A remplir
**PATCH** | /api/users/ | user_id | / | 200 OK<br> 403 Priviledge required <br> 404 Ressource not found<br> 409 Unique constraint violation | A remplir
**DELETE** | /api/users/ | user_id | A remplir | 200 OK<br> 403 Priviledge required <br> 404 Ressource not found | A remplir

404	
Resource not found

409	
Unique constraint violation

</details>


## HOW TO INSTALL AND USE KO.TOOLS
**Requirements**
**Seed**
**Run on local**
**Deploy with docker** (incoming)