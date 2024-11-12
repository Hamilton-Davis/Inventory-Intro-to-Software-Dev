import os
from cryptography.fernet import Fernet

# Paths to the encryption keys for username and password
USERNAME_KEY_FILE_PATH = "username.key"
PASSWORD_KEY_FILE_PATH = "password.key"


def generate_key(file_path):
    """
    Generate a new key for encryption and store it in the specified key file.
    """
    key = Fernet.generate_key()
    with open(file_path, "wb") as key_file:
        key_file.write(key)


def load_key(file_path):
    """
    Load the encryption key from the specified key file. Generate one if it doesn't exist.
    """
    if not os.path.exists(file_path):
        generate_key(file_path)
    with open(file_path, "rb") as key_file:
        return key_file.read()


# Load separate ciphers for username and password encryption
username_cipher = Fernet(load_key(USERNAME_KEY_FILE_PATH))
password_cipher = Fernet(load_key(PASSWORD_KEY_FILE_PATH))


def encrypt_username(data):
    """
    Encrypt the username using the username-specific cipher.
    :param data: Username to be encrypted (str).
    :return: Encrypted username (bytes).
    """
    return username_cipher.encrypt(data.encode())


def decrypt_username(encrypted_data):
    """
    Decrypt the encrypted username.
    :param encrypted_data: Encrypted username (bytes).
    :return: Decrypted username (str).
    """
    return username_cipher.decrypt(encrypted_data).decode()


def encrypt_password(data):
    """
    Encrypt the password using the password-specific cipher.
    :param data: Password to be encrypted (str).
    :return: Encrypted password (bytes).
    """
    return password_cipher.encrypt(data.encode())


def decrypt_password(encrypted_data):
    """
    Decrypt the encrypted password.
    :param encrypted_data: Encrypted password (bytes).
    :return: Decrypted password (str).
    """
    return password_cipher.decrypt(encrypted_data).decode()
