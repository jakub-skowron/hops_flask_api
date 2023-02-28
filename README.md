# HOPS FLASK API

### Installation guide (local machine):

Install Python 3.10.6:

- Download the Python 3.10.6 installer for your operating system from the official Python website: https://www.python.org/downloads/
Run the installer and follow the prompts to complete the installation.

Clone the repository:

- Open a terminal or command prompt window.
Navigate to the directory where you want to store your Flask application.
Clone the repository by running the command `git clone https://github.com/Jaqbek95/hops_flask_api.git`.

Create a virtual environment:

- Open a terminal or command prompt window.
Navigate to the root directory of your Flask application.
Create a virtual environment by running the command `$ python -m venv venv`. This will create a new directory named `venv` in your project directory.
Activate the virtual environment by running the command `source venv/bin/activate`.

Install packages from `requirements.txt`:

- Ensure that your virtual environment is active.
Run the command `pip install -r requirements.txt` to install all the packages listed in the `requirements.txt` file.

Create your local database:

- Open a terminal and run `flask shell`. Execute following code: 
```
>>> from src import db
>>> db.create_all()
 ```

That's it! You can use Hops API on your local machine by `python3 app.py` command in your terminal.