1. Prerequisites:
- PyCharm for Professionals
- PostgresSQL (Use default configurations, KNOW YOUR PASSWORD)
- Python installed on OS (3.9+)
- Git and GitHub

2. Creating a New Django Project in PyCharm
a. Open PyCharm -> New Project
b. Choose Django
c. Set the following:
- Location: your project folder
- (Note: if not done already, can create a Git repo by checking the respective box)
- Interpreter type: Project venv
- Under Advance Settings, Check "Enable Django Admin"

3. Install the requirements
- In terminal type: pip install psycopg2-binary

4. Adjust DATABASES dictionary in settings.py
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'postgres',
'USER': 'postgres', 'PASSWORD': 'yourpassword', 'HOST': 'localhost', 'PORT': '5432', } }

5. Make Migrations
In terminal type the following:
- python manage.py makemigrations
- python mange.py migrate

6. Run the Server (Development)
Do either the following:
- Hit the run button for your project folder
- Type in terminal: python manage.py runserver