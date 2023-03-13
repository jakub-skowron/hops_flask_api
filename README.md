# HOPS FLASK API

## Installation guide (docker-compose):

Install:
- Docker (version 23.0.1 or later)
- Docker Compose (version v2.15.1 or later)

Clone the repository:

- Open a terminal or command prompt window.
Navigate to the directory where you want to store your Flask application.
Clone the repository by running the following: 
```
$ git clone https://github.com/Jaqbek95/hops_flask_api.git
```

Use docker-compose to create and run containers:

- Open a terminal or command prompt window.
Navigate to the root directory of your Flask application.
Use commands as following:
```
$ docker compose up --build
```

 - To stop the app and its containers, press Ctrl + C in the terminal where docker-compose up is running. You can also stop and remove containers by following:
```
$ docker compose down
```

Configuration:

- The app can be configured using environment variables. See the docker-compose.yml file for the available options.

## Installation guide (local machine):

Install Python 3.10.6:

- Download the Python 3.10.6 installer for your operating system from the official Python website: https://www.python.org/downloads/
Run the installer and follow the prompts to complete the installation.

Clone the repository:

- Open a terminal or command prompt window.
Navigate to the directory where you want to store your Flask application.
Clone the repository by running the following: 
```
$ git clone https://github.com/Jaqbek95/hops_flask_api.git
```

Create a virtual environment:

- Open a terminal or command prompt window.
Navigate to the root directory of your Flask application.
Create a virtual environment and activate it by following:
```
$ python -m venv venv
$ source venv/bin/activate
```

Install packages from `requirements.txt`:

- Ensure that your virtual environment is active and install all packages by the following:
```
$ pip install -r requirements.txt
```

That's it! You can use Hops API on your local machine by running the following: 
```
$ python3 app.py
```
## License

This project is licensed under the MIT License - see the LICENSE file for details.
