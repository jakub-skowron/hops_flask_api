from os import environ
from src import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=environ.get("DEBUG") == "1")