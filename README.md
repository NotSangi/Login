# Flask Basic Test Project

This project is a basic test using Flask, a lightweight Python microframework. It demonstrates the use of several useful Flask libraries, including:

` flask_login ` for user session management 

` flask_bcrypt ` for encryption

` flask_migrate ` for database migrations

` flask_wtf ` for handling forms


The project also takes advantage of Flask Blueprints to organize and structure URLs. Although only one blueprint is implemented, it helps illustrate how blueprints work in larger applications.

A small amount of SCSS is used as a CSS preprocessor to keep the styling code organized and maintainable.

The database used is SQLite, which is ideal for this small-scale test since it doesn’t require complex relationships.

## Installation

To install all required libraries, run the following command from the project root:

`pip install -r requirements.txt` (The file is in root folder) 

## Create .env

The project uses a .env file to store essential configuration values.
This file contains:

- The<strong> secret key 🔐</strong>required for Flask and form handling to function correctly.

- The<strong> database path </strong>, which defines where the SQLite file will be created. 

### Example

```
SECRET_KEY = your_secret_key
DB_URI = "sqlite:///loginbd.sqlite"
```
## Migrations

This project uses Flask-Migrate, an extension that handles SQLAlchemy database migrations through Alembic.

Before running any migration commands, make sure you have properly configured the database URI in your .env file.

Follow these steps in your terminal:

### 1. Set the flask aplication

You must tell Flask which application to use, so run the following command

#### - On Windows

`set FLASK_APP=app.py`

#### - On macOS/Linux 

`export FLASK_APP=app.py `

### 2. Initialize migrations

Create the migrations/ folder that will store Alembic migration scripts.

`flask db init` 

### 3. Generate a new migration

Automatically detect model changes and generate a migration script.

`flask db migrate -m "Initial migration"` 

### 4. Apply migrations

Apply all pending migrations to the database.

`flask db upgrade`

### Important
Whenever you modify or add new models, repeat steps 3 and 4 to keep your database schema up to date.

## Running the Project

To start the application, simply execute the app.py file located in the project root:

`python app.py`

