import json
import os
import base64
from encryption import encrypt_username, decrypt_username, encrypt_password, decrypt_password, encrypt_hint, decrypt_hint

DATA_FILE_PATH = "user_data.json"

def load_user_data():
    """
    Load user data from a JSON file. If the file does not exist, return default credentials.
    """
    if not os.path.exists(DATA_FILE_PATH):
        return {"username": "admin", "password": "password", "hint": "", "answer": ""}

    with open(DATA_FILE_PATH, "r") as file:
        encrypted_data = json.load(file)

    try:
        # Decrypt each field using the respective decryption functions
        username = decrypt_username(base64.b64decode(encrypted_data["username"]))
        password = decrypt_password(base64.b64decode(encrypted_data["password"]))
        hint = decrypt_hint(base64.b64decode(encrypted_data["hint"]))
        answer = decrypt_hint(base64.b64decode(encrypted_data["answer"]))
        return {"username": username, "password": password, "hint": hint, "answer": answer}
    except Exception as e:
        print(f"Error loading user data: {e}. Resetting to default credentials.")
        return {"username": "admin", "password": "password", "hint": "", "answer": ""}

def save_user_data(username, password, hint, answer):
    """
    Save the encrypted username, password, hint, and answer to the JSON file.
    """
    # Encrypt each field separately and then encode to Base64 for JSON compatibility
    encrypted_username = base64.b64encode(encrypt_username(username)).decode('utf-8')
    encrypted_password = base64.b64encode(encrypt_password(password)).decode('utf-8')
    encrypted_hint = base64.b64encode(encrypt_hint(hint)).decode('utf-8')
    encrypted_answer = base64.b64encode(encrypt_hint(answer)).decode('utf-8')

    with open(DATA_FILE_PATH, "w") as file:
        # Save encrypted data as a JSON object
        json.dump({
            "username": encrypted_username,
            "password": encrypted_password,
            "hint": encrypted_hint,
            "answer": encrypted_answer
        }, file)

