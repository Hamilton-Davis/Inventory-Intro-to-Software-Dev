import json
import os

# File path for storing user data
DATA_FILE_PATH = "user_data.json"


def load_user_data():
    """
    Load user data from a JSON file. If the file does not exist, return default credentials.
    """
    if not os.path.exists(DATA_FILE_PATH):
        # Return default credentials if the file doesn't exist
        return {"username": "admin", "password": "password"}

    with open(DATA_FILE_PATH, "r") as file:
        return json.load(file)


def save_user_data(username, password):
    """
    Save the updated username and password to the JSON file.
    """
    with open(DATA_FILE_PATH, "w") as file:
        json.dump({"username": username, "password": password}, file)