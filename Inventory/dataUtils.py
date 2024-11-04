import json
import os
import base64
from encryption import encrypt_data, decrypt_data

DATA_FILE_PATH = "user_data.json"

def load_user_data():
    """
    Load user data from a JSON file. If the file does not exist, return default credentials.
    """
    if not os.path.exists(DATA_FILE_PATH):
        return {"username": "admin", "password": "password"}

    with open(DATA_FILE_PATH, "r") as file:
        encrypted_data = json.load(file)

    # Decode Base64 to get original encrypted bytes, then decrypt
    try:
        username = decrypt_data(base64.b64decode(encrypted_data["username"]))
        password = decrypt_data(base64.b64decode(encrypted_data["password"]))
        return {"username": username, "password": password}
    except Exception as e:
        print(f"Error loading user data: {e}. Resetting to default credentials.")
        return {"username": "admin", "password": "password"}

def save_user_data(username, password):
    """
    Save the encrypted username and password to the JSON file.
    """
    # Encrypt and then encode the result to Base64 for JSON compatibility
    encrypted_username = base64.b64encode(encrypt_data(username)).decode('utf-8')
    encrypted_password = base64.b64encode(encrypt_data(password)).decode('utf-8')

    with open(DATA_FILE_PATH, "w") as file:
        json.dump({"username": encrypted_username, "password": encrypted_password}, file)
