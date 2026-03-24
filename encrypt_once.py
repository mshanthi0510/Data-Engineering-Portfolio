from password_utils import encrypt_password
from cryptography.fernet import Fernet

def generate_keys():
    key = Fernet.generate_key()
    with open("secret.key","wb") as f:
        f.write(key)
    print("key saved successfully")

if __name__ == "__main__":
    #Uncomment this only for fists time
    generate_keys()

    e = input("Enter password:")
    encrypted = encrypt_password(e)
    print("Encrypted password (copy to password.utils)")
    print(encrypted)
