<h2>Developed by FEARLESS</h2>
<h3>RESTful API in which a client can do various CRUD operations on an Item Object</h3>

Technologies required/used for this Application:
- Python (Language) https://www.python.org/downloads/, 
- Django WEB Framework (Python Framework) https://docs.djangoproject.com/en/4.1/, 
- Django REST Framework (Python Framework) https://www.django-rest-framework.org/,
- Docker (Container) https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/,
- Docker Desktop App https://docs.docker.com/get-docker/,
- PostgreSQL (Database),
- Visual Studio Code (Text-Editor) https://code.visualstudio.com/Download

Application Details:
- Formatted for Docker containerization, 
- Contains a PostgreSQL database,
- runs on port:3000 automatically 

<h2>INSTALLTION / INITIAL SET UP GUIDLINES</h2><br>
<b>SECTION 1: CLONE PROJECT / INITIAL TERMINAL SETUP ON VSC </b><br>
1.	Open a new window in VSC<br>
2.	Open the command palette (crtl+shift+p)<br>
3.	Search for, and then select git clone (download extension if necessary)<br>
4.	Enter the following link (https://github.com/chetrambassit121/fearless_restful_api.git)<br> 
5.	Select, or create a new, repository location for this clone to be saved in<br>
6.	Open the repository in VSC<br>
7.	Open a new Terminal (crtl+shift+`)<br>
8.	Create a new virtual environment. ‘python -m venv venv’ (make sure you create while being within the directory. Enter the ‘cd ..’ command in the terminal if needed)<br>
9.	Activate the virtual environment, ‘venv/Scripts/activate’<br>
10.	Change directory to project folder ‘cd fearless/’<br><br>


<b>MUST DO SECTION 1<br>
SECTION 2: DOCKER COMMANDS TO START/INITIAL BUILD OF CONTAINER/IMAGE:</b><br>
11.	 Open up the Docker Desktop App (download if necessary)<br>
12.	 Enter the command ‘docker-compose ’, this will start or execute the initial build of the container/image. Leave this terminal running.<br>
13.	 Open up, and select, a new terminal (split with VSC). Repeat steps 9-10 if necessary.<br>

<br>MUST DO SECTION 2<br>
SECTION 3: PYTHON MAKEMIGRATIONS/MIGRATE COMMANDS THROUGH DOCKER</b><br>
14.	 Enter the command ‘docker-compose run --rm web python manage.py makemigrations’<br>
15.	 Enter the command ‘docker-compose run --rm web python manage.py migrate’<br>

<b>MUST DO SECTION 3<br>
SECTON 4: RUN PYTHON SERVER THROUGH DOCKER</b><br>
16.	Enter the command ‘docker-compose run --rm web python manage.py runserver’<br>
17.	Open up localhost:3000 in your browser<br>


<b>SECTION 5: GET DOCKER CONTAINER ID / CREATE A SUPERUSER</b><br>
18.	Enter the command ‘docker ps -aqf "name=fearless"’ to get the container id. (Two id’s will appear)<br>
19.	Copy the id on the top row<br>
20.	Enter the command ‘docker exec -it <container_id> python manage.py createsuperuser’<br>
21.	Fill in form<br>


<b>SECTION 6: INSTALLING OTHER APPS or LIBRARIES / FREEZING INTO REQUIREMENTS</b><br>
22.	Enter the command ‘docker-compose run --rm web pip install <name>’<br>
23.	Enter the command ‘docker-compose run --rm web pip freeze > requirements.txt’<br>

  
<b><h3>CONCLUSION:</h3></b>
This RESTful API is now connected locally to you Docker Desktop App and can be accessed on localhost:3000<br>

<b><h3>General Commands/Edits after installation/initial set up</h3></b>
1. To start the server and have access to localhost:3000, enter the command 'docker-compose up'<br>
2. To run the server on a specfic port number, enter the command 'docker-compose run --rm web python manage.py runserver port_number'<br>
3. To change the port number manully go to Docker-compose.yml, under web:/commands and web:/ports<br>
4. To exit from Docker enter crtl+c
  







