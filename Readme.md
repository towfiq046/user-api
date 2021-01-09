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

POST: /parent

PUT: /parent/<int:parent_id>

DELETE: /parent/<int:parent_id>
```

* API for child user:

```bash
GET: /parent/<int:parent_id>/child

POST: /parent/<int:parent_id>/child

PUT: /parent/<int:parent_id>/child/<int:child_id>

DELETE: /parent/<int:parent_id>/child/<int:child_id>
```


User data for parent:

`{
  "first_name": "Towfiq",
  "last_name": "Ahmed",
  "state": "bd",
  "city": "Khulna",
  "street": "Rasulbag",
  "zip_code": 5245
}`

User data for child:

`{
  "first_name": "Towfiq",
  "last_name": "Ahmed"
}`

Applications required to run this app:

* To input data download postman form here (<https://www.postman.com/downloads/>)
* Python 3.9 (<https://www.python.org/downloads/>)
  * Note: Check the `Add python 3.9 to PATH` box on the installation stage

## Run the project

* `cd` to the project directory
* Execute `pip install pipenv`
* Execute the command `pipenv install` to install all the dependencies
* Now run the project with `python app.py` command
