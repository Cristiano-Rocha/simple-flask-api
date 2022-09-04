# A simple Flask API

This a simple api built with [Flask](https://flask.palletsprojects.com/en/2.2.x/) microframework

## Tecnologies used
* **[Pyhon3](https://www.python.org/downloads/)** Python is a programminglanguage that lets you work quickllu and integrate more effectively
* **[Flask](flask.pocoo.org/)** Flask is a microframework written in Python
* **[Poetry](https://python-poetry.org/)** Python Packaging and dependency management
* **[Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/e)** Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application
* **[Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)** Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic

* **[Docker](https://www.docker.com/)** Docker takes away repetitive, mundane configuration tasks and is used throughout the development lifecycle for fast, easy and portable application development
* **[Docker Compose](https://docs.docker.com/compose/)** Compose is a tool for defining and running multi-container Docker applications

## 🌱 How to start this project

## Endpoints
    GET /api/dog
    POST /api/dog
    DELETE /api/dog
    PUT /api/dog

### GET /api/dog

Will return all dogs record from database

```json
{
    "results": [
        {
            "name": "Pluto",
            "age": 10,
            "color": "brown",
            "gender": "male",
            "breed": "Bloodhound",
            "size": "large"

        },
        {...}
    ]
}
```

### POST /api/dog
Add a new dog to the database

```json
{
    "name": "Pluto",
    "age": 10,
    "color": "brown",
    "gender": "male",
    "breed": "Bloodhound",
    "size": "large"
}
```

### DELETE /api/dog/\<int:id\>
Delete an existing record with the specific id

### PUT /api/dog/\<int:id\>
Update an existing record with the specific id
```json
{
    "name": "Pluto",
    "age": 11,
    "color": "brown",
    "gender": "male",
    "breed": "Bloodhound",
    "size": "large"
}
```

