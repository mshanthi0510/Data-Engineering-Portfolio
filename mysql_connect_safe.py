import mysql.connector
from password_utils import get_decrypt_password

def connect_to_mysql():
    conn = mysql.connector.connect(
        host ="localhost",
        user="root",
        password = get_decrypt_password(),
        database = "test"
    )
    print("Connection is successful")
    #print(get_decrypt_password())
    conn.close

if __name__== "__main__":
    connect_to_mysql()