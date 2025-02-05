# Django Project Example
## 1. Name
   **Learning Log**  
## 2. Development of specifications
A web application called Learning Log, allowing users to:
- record information of interest
- add journal entries while exploring a particular topic. 

The homepage of the Learning Log application should:
- include a description explaining the purpose of this website
- encourage users to register or log in.

After logging in, users should be able to:
- create a new topic,
- add a new entry and read
- edit existing entries.
## 3. Creating a virtual environment
Create a new directory for the project and name it learning_log. 

In the shell, navigate to the newly created directory and then create a virtual environment.
```
python3 -m venv ll_env
source ll_env/bin/activate
```
## 4. Installation of the Django framework
```
pip install --upgrade pip
pip install django
```
## 5. Creating a project in Django
```
django-admin startproject ll_project .
```
## 6. Creating a database
```
python manage.py migrate
```
## 7. Project 
```
python manage.py runserver
```
