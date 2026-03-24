from cryptography.fernet import Fernet

class FakeStr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

def load_key():
    return open("secret.key","rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)

def get_decrypt_password():
    encrypted_password = input("Enter the encrypted password:")
    return decrypt_password(encrypted_password)
