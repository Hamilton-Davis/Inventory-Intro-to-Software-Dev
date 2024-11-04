import os

from cryptography.fernet import Fernet

# Path to the encryption key
KEY_FILE_PATH = "secret.key"


def generate_key():
    """
    Generate a new key for encryption and store it in the key file.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE_PATH, "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the encryption key from the key file. Generate one if it doesn't exist.
    """
    if not os.path.exists(KEY_FILE_PATH):
        generate_key()
    with open(KEY_FILE_PATH, "rb") as key_file:
        return key_file.read()


# Initialize Fernet with the loaded key
cipher = Fernet(load_key())


def encrypt_data(data):
    """
    Encrypt data (such as username or password).
    :param data: Data to be encrypted (str).
    :return: Encrypted data (bytes).
    """
    return cipher.encrypt(data.encode())


def decrypt_data(encrypted_data):
    """
    Decrypt encrypted data.
    :param encrypted_data: Data to be decrypted (bytes).
    :return: Decrypted data (str).
    """
    return cipher.decrypt(encrypted_data).decode()
