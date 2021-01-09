# APP for storing user data

## Overview of this app

This app stores given user data to database

This app has two User types

1. Parent User
2. Child User

Parent User can have address but the Child User can not have any address of it's own and it belongs to a parent

* API for parent user:

```bash
GET: /parent

GET: /parent/<int:parent_id>

POST: /parent

PUT: /parent/<int:parent_id>

DELETE: /parent/<int:parent_id>
```

* API for child user:

```bash
GET: /child

GET: /parent/<int:parent_id>/child

POST: /parent/<int:parent_id>/child

PUT: /parent/<int:parent_id>/child/<int:child_id>

DELETE: /parent/<int:parent_id>/child/<int:child_id>
```

User data example for parent:

`{
  "first_name": "Towfiq",
  "last_name": "Ahmed",
  "state": "bd",
  "city": "Khulna",
  "street": "Rasulbag",
  "zip_code": 5245
}`

User data example for child:

`{
  "first_name": "Towfiq",
  "last_name": "Ahmed"
}`

Applications required to run this app:

* Python 3.9 (<https://www.python.org/downloads/>)
  * Note: Check the `Add python 3.9 to PATH` box on the installation stage
* Execute `pip install pipenv`

## Run the project

* `cd` to the project directory
* Execute the command `pipenv install` to install all the dependencies
* Now run the project with `python app.py` command
