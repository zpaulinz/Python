1. Name
2. Development of specifications
3. Creating a virtual environment
4. Installation of the Django framework
5. Creating a project in Django
6. Creating a database
7. Project overview


    For example:
        1. name: Learning Log

        2. specifications: 
            A web application called Learning Log, allowing users to record information of  interest and thus add journal entries while exploring a particular topic.
            The homepage of the Learning Log application should include 
            a description explaining the purpose of this website and encourage users to register or log in.
            After logging in, users should be able to create a new topic, 
            add a new entry, as well as read and edit existing entries.

        3. virtual environment:
            Create a new directory for the project and name it learning_log.
            In the shell, navigate to the newly created directory 
            and then create a virtual environment.
            python3 -m venv ll_env
            source ll_env/bin/activate

        4. install Django:
            pip install --upgrade pip
            pip install django

        5. creating a project:
            django-admin startproject ll_project .

        6. creating a database:
            python manage.py migrate
            
        7. project overview:
            python manage.py runserver