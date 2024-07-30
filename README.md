# user_management_system
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white)

This is a simple user management system that allows you to add, delete, and update users.
It is built using Python and Flask.

## Folder Structure
```commandline
app
│     config
│   │   config.py
│   │   database_config.py
│   │   logging_config.py
│    controller
│   │   __init__.py
│   │   user_controller.py
│   entity
│   │   user_entity.py
│   exception
│   │   base_exception.py
│   │   db_operation.py
│   │   exception_handler.py
│   model
│   │   generic_responses.py
│   │   user_model.py
│   service
│   │   http_service.py
│   │   user_service.py
│   repository
│   │   user_repository.py
│   util
│   │   auth.py
│   test
main.py
requirements.txt
README.md
secret_key.env
```

## Folder Structure Description
- `config`: Contains the configuration files for the database
- `controller`: Contains the controller/API files for the user
- `entity`: Contains the files which database connection using SQLAlchemy and ORM
- `exception`: Contains the exception handler files
- `model`: Contains the response models
- `service`: Contains the files which contain the business logic
- `repository`: Contains the files which contain the database operations
- `util`: Contains the utility files
- `test`: Contains the test files
- `main.py`: Contains the configuration to run the application

## Databse Configuration
change with your database configuration in `config.py` file
```commandline
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB_NAME = 'user_management'
```

Table name : `user`

columns_name : `id`, `username`, `email`, `hashed_password`, `created_at`

secret_key.env : contains the secret key for JWT token

## Packages
```commandline
pip install fastapi
pip install uvicorn
pip install pydantic
pip install sqlalchemy
pip install pymysql
pip install requests
pip install "passlib[bcrypt]"
pip install --upgrade bcrypt==4.0.1
pip install pyJWT
```

## Installation
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Connect to the database by updating the `config.py` file
4. Create database, table and columns refer `config.py and user_entity.py`
5. Run the application using `uvicorn main:app --reload`

