import mysql.connector

def connectToServer(host, user_name, password=''):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user_name,
            passwd=password
        )
        print("MySQL Database Connection Successfully Established")
    except Exception as err:
        print(f"Error: {err}")
    
    return connection

db = connectToServer("localhost", "root")

cursor = db.cursor()
cursor.execute("create database practice")
cursor.execute("show databases")
for i in cursor:
    print(i)