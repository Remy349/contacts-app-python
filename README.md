# ContactsApp with Python and Flask

ContactsApp is a CRUD in which you can create, read, update and delete the contacts you enter. But before you get access to these features you must create a user for the website, which will contain a username, email and password to authenticate.

But not only you can save and have a list of your contacts in this basic CRUD, the site also has an API developed following the REST architecture, at least try to create a functional REST API.

## Table of Contents:

- [Technologies used in the development](#technologies-used-in-the-development)
- [How to execute it](#how-to-execute-it)
- [How to use the api](#how-to-use-the-api)

## Technologies used in the development
It was developed using Python(3.9.6) and Flask for the development of the server and Postgresql was used as database.

To handle the queries I used the ORM model with SQLAlchemy using Flask-SQLAlchemy for Flask.

For the client side just use the basics, HTML, SASS and a bit of JS for some useful little features.

## How to execute it
Great, if you want to run the project from your own computer, do the following:

1. You must have Python installed on your computer and have a Postgresql database, it can be obtained from a service like Heroku, Render, Railway or a database that is running on your own computer, just get the free plan from these services and you will have a Postgresql database immediately. Here are the links to these services:
- [Heroku](https://www.heroku.com/)
- [Render](https://render.com/)
- [Railway](https://railway.app/)

2. Download the repository and move to the repository's root folder. If you have Git, do the following:
```Shell
# Clone the repository
$ git clone https://github.com/Remy349/contacts-app-python.git

# Move to the repository folder
$ cd contacts-app-python
```

3. Once placed in the repository folder activate a Python development/virtual environment as follows:
```Shell
# For Linux(This will depend on the version of Python you have)
# I use Python3.9.6 so I use python3.9 -m venv venv
$ python3 -m venv venv
# Now activate the virtual environment
$ . venv/bin/activate

# For Windows(py -3 -m venv venv or...)
$ python -m venv venv
# Now activate the virtual environment
$ venv\Scripts\activate
```

4. Now that you have an active virtual environment, install the necessary requirements from the "requirements.txt" file to run the project:
```Shell
# If you have already installed Python on your computer, you probably have Pip installed automatically.
# For Windows could be just "pip"
(venv) $ pip3 install -r requirements.txt
```

## How to use the api
