# TodoApi
Todo App
To-Do List Application
# Description
It is a To-Do Application developed with Django Rest Framework.

# End Points
- GET   /api/tasks/    ?start_date=&end_date=
- POST  /api/tasks/
- PUT   /api/tasks/:id/
- PATCH   /api/tasks/:id/
- DELETE   /api/tasks/:id/
- GET   /api/tasks/todo/
- GET   /api/tasks/expired/
- GET   /api/tasks/in_progress/
- GET   /api/tasks/done/

# Get the code
- Clone the repository git clone  https://github.com/TemurWebDev/TodoApi.git

# Install the project dependencies
- First create virtualenv, then enter the following command.
- pip install -r requirements.txt

# Run the commands to generate the database
- python manage.py makemigrations
- python manage.py migrate

# Generate super user
python manage.py createsuperuser

# Run the server
python manage.py runserver the application will be running on port 8000 http://0.0.0.0:8000/

# Run the test
python manage.py test


