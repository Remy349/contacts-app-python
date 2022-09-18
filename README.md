# ContactsApp with Python and Flask

ContactsApp is a CRUD in which you can create, read, update and delete the contacts you enter. But before you get access to these features you must create a user for the website, which will contain a username, email and password to authenticate.

But not only you can save and have a list of your contacts in this basic CRUD, the site also has an API developed following the REST architecture, at least try to create a functional REST API.

## Table of Contents:

- [Technologies used in the development](#technologies-used-in-the-development)
- [How to execute it](#how-to-execute-it)
- [How to use the API](#how-to-use-the-api)

## Technologies used in the development
It was developed using Python(3.9.6) and Flask for the development of the server and Postgresql was used as database.

To handle the queries I used the ORM model with SQLAlchemy using Flask-SQLAlchemy for Flask.

For the client side just use the basics, HTML, SASS and a bit of JS for some useful little features.

## How to execute it
Great, if you want to run the project from your own computer, do the following:

1. You must have Python installed on your computer and have a Postgresql database, it can be obtained from a service like Heroku, Render, Railway or a database that is running on your own computer, just get the free plan from these services and you will have a Postgresql database immediately. Here are the links to these services:
- [Heroku](https://www.heroku.com/)
- [Render](https://render.com/)
- [Railway](https://railway.app/) (Recommended to obtain the database quickly)

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

5. After this you will be ready to run the application, but first create an ".env" file in the main folder of the project to save your environment variables, inside this file you will need the following:
```Shell
# .env

SECRET_KEY=yourownsecretkey
# Connection to the database(Postgresql) example:
DATABASE_URL=postgres://postgres:mypassword@localhost:5432/database-name
```

6. Now just run the following commands in the terminal to add the tables to the database and run the server:
```Shell
# Adding table models to the database
(venv) $ flask db upgrade

# Run the server
(venv) $ flask run
* Serving Flask app 'application.py'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

7. Enjoy the application

## How to use the API
With the API you will be able to perform queries to obtain data from the user table of the database.

As a first step you must create a user in the application in order to generate a unique token for you and be able to make requests to the API. After you have created a user you will be able to generate your own token as follows:

The requests can be made from the terminal, the project comes with HTTPie installed, a command-line HTTP client written in Python that makes it easy to send API requests
```Shell
# Generate a unique token
(venv) $ http --auth username:password POST http://localhost:5000/api/tokens
# You will see something like this
HTTP/1.1 200 OK
Connection: close
Content-Length: 50
Content-Type: application/json
Date: Sun, 18 Sep 2022 18:43:22 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "token": "iDnAZ41h6VSgLtiUwg6AwJGa3dECcoIh"
}
```

Now that you have obtained your personal token (1 hour duration) you will be able to make the following API requests:
```Shell
# Get the information of individual users using the id of the user you want to get the information from
(venv) $ http GET http://localhost:5000/api/users/<id> Authorization:"Bearer iDnAZ41h6VSgLtiUwg6AwJGa3dECcoIh"
# You will see something like this
HTTP/1.1 200 OK
Connection: close
Content-Length: 207
Content-Type: application/json
Date: Sun, 18 Sep 2022 18:44:12 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "_links": {
        "avatar": "https://www.gravatar.com/avatar/88f8346dbd55de39420599ae583ac3ad?default=identicon",
        "self": "/api/users/1"
    },
    "contacts_count": 7,
    "id": 1,
    "username": "SantyM"
}
```

```Shell
# Get the information of all registered users
(venv) $ http GET http://localhost:5000/api/users Authorization:"Bearer iDnAZ41h6VSgLtiUwg6AwJGa3dECcoIh"
# You will see something like this
HTTP/1.1 200 OK
Connection: close
Content-Length: 2680
Content-Type: application/json
Date: Sun, 18 Sep 2022 18:45:50 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "_links": {
        "next": "/api/users?page=2&per_page=10",
        "prev": null,
        "self": "/api/users?page=1&per_page=10"
    },
    "_meta": {
        "page": 1,
        "per_page": 10,
        "total_items": 12,
        "total_pages": 2
    },
    "items": [
        {
            "_links": {
                "avatar": "https://www.gravatar.com/avatar/aa99b351245441b8ca95d54a52d2998c?default=identicon",
                "self": "/api/users/3"
            },
            "contacts_count": 0,
            "id": 3,
            "username": "Test1"
        },
        ............
```

```Shell
# Register a new user (Token is not required)
(venv) $ http POST http://localhost:5000/api/users username="sasasa" email="sasasa@example.com" password="sasasa"
# You will see something like this
HTTP/1.1 201 CREATED
Connection: close
Content-Length: 209
Content-Type: application/json
Date: Sun, 18 Sep 2022 18:40:02 GMT
Location: /api/users/12
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "_links": {
        "avatar": "https://www.gravatar.com/avatar/a75b79ed95589d71210b4a1b1de80adf?default=identicon",
        "self": "/api/users/12"
    },
    "contacts_count": 0,
    "id": 12,
    "username": "sasasa"
}
```

```Shell
# Finally you can delete your token to generate another one, this if your token has already expired
(venv) $ http DELETE http://localhost:5000/api/tokens Authorization:"Bearer iDnAZ41h6VSgLtiUwg6AwJGa3dECcoIh"
# You will see something like this
HTTP/1.1 204 NO CONTENT
Connection: close
Content-Type: text/html; charset=utf-8
Date: Sun, 18 Sep 2022 18:52:45 GMT
Server: Werkzeug/2.2.2 Python/3.9.6
```

### Developed by Santiago de Jesús Moraga Caldera - Remy349(GitHub)
