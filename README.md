# api-dojo-python
This project is aimed to create a API using DRF during a dojo.
The API is gonna create a Todo API.

## Functions

Todo
- description: string
- done: boolean

Functionalities
- Add a new todo(description, done): done should not appear or be accept during a post.
- Update a todo: update description and/or done field.
- Get a list of todo's.

## Start to develop

It's a good practice to use a virtual environment.

If you doesn't have '''virtualenv''', use the command '''pip install virtualenv'''.

And at project folder run '''virtualenv env'''. This is gonna create a folder env inside the actual folder.

To start the virtual environment run '''source env/bin/activate'''.
To end the virtual environment run deactivate.

### Necessary libs for develop a API

'''pip install django djangorestframework'''

The command above is gonna install django and djangorestframework.

### Run tests

'''manage.py test''' on todo folder.

