# WriteSphere - Full Django Project Scaffold (MySQL & PythonAnywhere ready)
## Overview
This scaffold contains a Django project prepared for MySQL usage and PythonAnywhere deployment.
Features included:
- User registration/login/profile
- Role groups (Admin, Author, Reader)
- Posts with cover image, category, tags, timestamps
- Likes and Follow models, Comment system
- Static & media configuration, .env support via python-dotenv
- Admin customization for Post listing
## Quick local setup
1. Unzip and open the project folder.
2. Create and activate virtualenv:
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)
3. Install requirements:
   pip install -r requirements.txt
4. Copy .env.example to .env and edit values.
5. Run migrations and create superuser:
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py loaddata (optional)
   python manage.py create_roles
6. Run server:
   python manage.py runserver
## Using MySQL & Deploy on PythonAnywhere
1. Set USE_MYSQL=True in .env and configure MYSQL_* env values.
2. On PythonAnywhere, create a MySQL database and enter credentials into .env (you can store env vars in Web > Environment variables).
3. Upload project to GitHub and clone on PythonAnywhere or push from local repo.
4. Run migrations on PythonAnywhere and collectstatic:
   python manage.py migrate
   python manage.py collectstatic
5. Configure the WSGI file on PythonAnywhere to point to writesphere.wsgi and set STATIC/MEDIA directories in Web tab.
## Notes
- For rich-text editing, integrate django-ckeditor or TinyMCE (not included by default).
- Remember to set DEBUG=False and replace SECRET_KEY in production.
