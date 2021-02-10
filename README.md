1. Create virtual environment by running setup.sh in setup folder.
  Command: sh setup.sh

2. Activate the virtualenv created in setup folder.
  Command: source venv/bin/activate

3. Install dependencies by running the below command.
  Command: pip install -r requirements.pip

4. Copy the assign.conf from setup folder to /etc/nginx/sites-enabled/ and update the path accordingly.

5. Restart nginx server.
  Command: sudo service nginx restart.

6. Navigate back to the path where manage.py present and run the below command.
  Command: python manage.py runserver

7. Please create the superuser by below command
  Command: python manage.py createsuperuser

8. In browser type localhost:9003 to check the application.

