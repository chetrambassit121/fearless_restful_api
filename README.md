<h2>Developed by FEARLESS</h2>
<h3>RESTful API in which a client can do various CRUD operations on an Item Object</h3>

Languages and Frameworks Used:
- Python, 
- Django WEB Framework, 
- Django REST Framework

<h2>INSTALLTION / INITIAL SET UP GUIDLINES</h2>


<b>SECTION 1: CLONE PROJECT / INITIAL TERMINAL SETUP ON VSC </b>
1.	Open new window in VSC
2.	Open command palette (crtl+shift+p)
3.	Search for and select git clone (download extension if necessary)
4.	Enter the following link (https://github.com/chetrambassit121/fearless_restful_api.git) 
5.	Select, or create a new, repository location
6.	Open the repository in VSC
7.	Open a new Terminal (crtl+shift+`)
8.	Create a new virtual environment. ‘python -m venv venv’ (make sure you create while being within the directory. Enter the ‘cd ..’ command in the terminal if needed.)
9.	Activate the virtual environment, ‘venv/Scripts/activate’
10.	Change directory to project folder ‘cd fearless/’<br>


MUST DO SECTION 1<br>
SECTION 2: DOCKER COMMANDS TO START/INITIAL BUILD OF CONTAINER/IMAGE:<br>
11.	 Open up the Docker Desktop App (download if necessary)<br>
12.	 Enter the command ‘docker-compose ’, this will start or execute the initial build of the container/image. Leave this terminal running.<br>
13.	 Open up, and select, a new terminal (split with VSC). Repeat steps 9-10 if necessary.<br>


MUST DO SECTION 2<br>
SECTION 3: PYTHON MAKEMIGRATIONS/MIGRATE COMMANDS THROUGH DOCKER<br>  
14.	 Enter the command ‘docker-compose run --rm web python manage.py makemigrations’<br>
15.	 Enter the command ‘docker-compose run --rm web python manage.py migrate’<br>

MUST DO SECTION 3<br>
SECTON 4: RUN PYTHON SERVER THROUGH DOCKER<br>
16.	Enter the command ‘docker-compose run --rm web python manage.py runserver’<br>
17.	Open up localhost:3000 in your browser<br>


SECTION 5: GET DOCKER CONTAINER ID / CREATE A SUPERUSER<br>
18.	Enter the command ‘docker ps -aqf "name=fearless"’ to get the container id. (Two id’s will appear)<br>
19.	Copy the id on the top row<br>
20.	Enter the command ‘docker exec -it <container_id> python manage.py createsuperuser’<br>
21.	Fill in form<br>


SECTION 6: INSTALLING OTHER APPS or LIBRARIES / FREEZING INTO REQUIREMENTS<br>
22.	Enter the command ‘docker-compose run --rm web pip install <name>’<br>
23.	Enter the command ‘docker-compose run --rm web pip freeze > requirements.txt’<br>




