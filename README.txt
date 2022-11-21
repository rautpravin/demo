1. Create a virtualenv using virtualenv command:
   > virtualenv [-p python3.x] venv   # [-p python3.x] is optional/

2. Activate the virtual environment.
   > source venv/bin/activate

3. install required python libs using pip.
   here, in our project we have requirements.txt file,
   > pip install -r requirements.txt

4. > python manage.py makemigrations

5. > python manage.py migrate

6. > python manage.py runserver
