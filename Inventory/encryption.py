import os
from cryptography.fernet import Fernet

# Paths to the encryption keys for username, password, hint, and answer
USERNAME_KEY_FILE_PATH = "username.key"
PASSWORD_KEY_FILE_PATH = "password.key"
HINT_KEY_FILE_PATH = "hint.key"
ANSWER_KEY_FILE_PATH = "answer.key"


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


# Load separate ciphers for username, password, hint, and answer encryption
username_cipher = Fernet(load_key(USERNAME_KEY_FILE_PATH))
password_cipher = Fernet(load_key(PASSWORD_KEY_FILE_PATH))
hint_cipher = Fernet(load_key(HINT_KEY_FILE_PATH))
answer_cipher = Fernet(load_key(ANSWER_KEY_FILE_PATH))


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


def encrypt_hint(data):
    """
    Encrypt the security hint using the hint-specific cipher.
    :param data: Hint to be encrypted (str).
    :return: Encrypted hint (bytes).
    """
    return hint_cipher.encrypt(data.encode())


def decrypt_hint(encrypted_data):
    """
    Decrypt the encrypted security hint.
    :param encrypted_data: Encrypted hint (bytes).
    :return: Decrypted hint (str).
    """
    return hint_cipher.decrypt(encrypted_data).decode()


def encrypt_answer(data):
    """
    Encrypt the answer to the security hint using the answer-specific cipher.
    :param data: Answer to be encrypted (str).
    :return: Encrypted answer (bytes).
    """
    return answer_cipher.encrypt(data.encode())


def decrypt_answer(encrypted_data):
    """
    Decrypt the encrypted answer to the security hint.
    :param encrypted_data: Encrypted answer (bytes).
    :return: Decrypted answer (str).
    """
    return answer_cipher.decrypt(encrypted_data).decode()
