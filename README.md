# Chatify #

## Project Setup ##

1) Clone the repository.

2) Open terminal and cd into the root project directory (where manage.py and requirements.txt file exists).

3) Create a new virtual environment with command: `python -m venv venv`

4) Activate the virtual environment using command(for Windows): `.\venv\Scripts\activate`

5) Install required python packages (including django) using requirements.txt file with command: `pip install -r requirements.txt`

6) Set up a database: Create a MySQL database/schema with the name "django_chatify".
Update the database credentials (user and password) in settings.py file.
7) As the project uses RabbitMQ as the channel layer for the chatting using websocket functionality, 
you will need to install RabbitMQ for it to work. Follow below steps to install it -
 - a) Download and install Erlang/OTP from - https://www.erlang.org/downloads (RabbitMQ requires Erlang to be installed).
 - b) Download and install RabbitMQ for windows from - https://www.rabbitmq.com/docs/install-windows#installer.
 - c) After installing, make sure to start the RabbitMQ server, you can do it by searching 'rabbitmq service - start' in the Windows search bar.

- You can also follow steps for installing RabbitMQ on their official page - https://www.rabbitmq.com/docs/install-windows#installer.

8) Run following commands for applying database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

9) Start the server with the command: `python manage.py runserver`

## Testing ##

1) Once the server is running, you can visit the application in your browser at - http://localhost:8000/chat/register/.
2) On register page, register 2 or more users for testing the chatting functionality.
3) After registering you can click on login link to go to login page and login with at least 2 users in different browser windows so that you can see the realtime chat between those 2 users.
4) After logging in with username and password, you should be able to see the list of users you just registered on the homepage.
5) You can send the request to any of the user.
6) The other user can see the received and sent requests in the Requests tab and also on the homepage in front of the users list.
7) Once the request is accepted, the Chat option will be enabled between these 2 users.
8) After clicking on the Chat button, the chat page will open and you can send and receive messages from a particular user.
