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
![Screenshot (1)](https://user-images.githubusercontent.com/75236091/210103569-721e76b0-04b0-49e9-a117-31d99ed85b53.png)<br><br>
2.	Open the command palette (crtl+shift+p)<br>
![Screenshot (2)](https://user-images.githubusercontent.com/75236091/210103818-759ead08-4740-422e-b7db-6272e33c1be0.png)<br><br>
3.	Search for, and then select git clone (download extension if necessary)<br>
![Screenshot (3)](https://user-images.githubusercontent.com/75236091/210103976-f9c35867-76cb-4da5-8a92-87dcb413df94.png)<br><br>
4.	Enter the following link (https://github.com/chetrambassit121/fearless_restful_api.git)<br> 
![Screenshot (4)](https://user-images.githubusercontent.com/75236091/210104106-44ff7e64-5c22-4d72-8627-6bea3a54cc4c.png)<br><br>
5.	Select, or create a new, repository location for this clone to be saved in<br>
![Screenshot (5)](https://user-images.githubusercontent.com/75236091/210104296-99b1cf40-cb77-4524-9e03-a781de5531b8.png)<br><br>
6.	Open the repository in VSC<br>![Screenshot (6)](https://user-images.githubusercontent.com/75236091/210104371-a8d200ad-08a8-4a7b-9e8f-4327f27cc2cc.png)<br><br>
7.	Open a new Terminal (crtl+shift+`)<br>
![Screenshot (7)](https://user-images.githubusercontent.com/75236091/210104445-32e76ffb-c94c-4ab5-8039-56dcae3eeb74.png)<br><br>
8.	Create a new virtual environment. ‘python -m venv venv’ (make sure you create while being within the directory. Enter the ‘cd ..’ command in the terminal if needed)<br>
9.	Activate the virtual environment, ‘venv/Scripts/activate’<br>
10.	Change directory to project folder ‘cd fearless/’<br>![Screenshot (8-10)](https://user-images.githubusercontent.com/75236091/210104809-8b05194d-d8c5-4ba7-9113-62f45a22155a.png)<br><br>


<b>MUST DO SECTION 1<br>
SECTION 2: DOCKER COMMANDS TO START/INITIAL BUILD OF CONTAINER/IMAGE:</b><br>
11.	 Open up the Docker Desktop App (download if necessary)<br>![Screenshot (9)](https://user-images.githubusercontent.com/75236091/210104917-252720c8-006d-4904-b3a0-52c7b7efe30e.png)<br><br>

12.	 Enter the command ‘docker-compose ’, this will start or execute the initial build of the container/image. Leave this terminal running.<br>![Screenshot (10)](https://user-images.githubusercontent.com/75236091/210105110-e5defd20-8954-41ed-a960-c99e62082e85.png)<br><br>
13.	 Open up, and select, a new terminal (split with VSC). Repeat steps 9-10 if necessary.<br>![Screenshot (11)](https://user-images.githubusercontent.com/75236091/210105383-88ee1010-ab9c-43dc-8724-d901913819d6.png)<br><br>


<br>MUST DO SECTION 2<br>
SECTION 3: PYTHON MAKEMIGRATIONS/MIGRATE COMMANDS THROUGH DOCKER</b><br>
14.	 Enter the command ‘docker-compose run --rm web python manage.py makemigrations’<br>
15.	 Enter the command ‘docker-compose run --rm web python manage.py migrate’<br>![Screenshot (12)](https://user-images.githubusercontent.com/75236091/210105582-dddab584-71a2-4c49-a538-e0778c69dc39.png)<br><br>

<b>MUST DO SECTION 3<br>
SECTON 4: RUN PYTHON SERVER THROUGH DOCKER</b><br>
16.	Exit the docker-compose, then enter the command ‘docker-compose run’<br>
17.	Open up localhost:3000 in your browser<br>![Screenshot (14)](https://user-images.githubusercontent.com/75236091/210105889-c9b1aa5b-c1ae-4365-b206-3d5f3363d53b.png)<br><br>


<b>SECTION 5: GET DOCKER CONTAINER ID / CREATE A SUPERUSER</b><br>
18.	Enter the command ‘docker ps -aqf "name=fearless_restful_api"’ to get the container id. (Two id’s will appear)<br>
19.	Copy the id on the top row<br>
20.	Enter the command ‘docker exec -it <container_id> python manage.py createsuperuser’<br>
21.	Fill in form<br>![Screenshot (15)](https://user-images.githubusercontent.com/75236091/210106281-932d028b-3416-4567-be94-8a33395e1890.png)<br><br>


<b>SECTION 6: INSTALLING OTHER APPS or LIBRARIES / FREEZING INTO REQUIREMENTS</b><br>
22.	Enter the command ‘docker-compose run --rm web pip install <name>’<br>
23.	Enter the command ‘docker-compose run --rm web pip freeze > requirements.txt’<br>![Screenshot (16)](https://user-images.githubusercontent.com/75236091/210106515-1f5c4e85-6918-41a5-809a-92a6c38e4931.png)<br><br>

  
<b><h3>CONCLUSION:</h3></b>
This RESTful API is now connected locally to you Docker Desktop App and can be accessed on localhost:3000<br>

<b><h3>General Commands/Edits after installation/initial set up</h3></b>
1. To start the server and have access to localhost:3000, enter the command 'docker-compose up'<br>
2. To run the server on a specfic port number, enter the command 'docker-compose run --rm web python manage.py runserver port_number'<br>
3. To change the port number manully go to Docker-compose.yml, under web:/commands and web:/ports<br>
4. To exit from Docker enter crtl+c
  







