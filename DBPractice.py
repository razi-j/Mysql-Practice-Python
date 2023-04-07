import mysql.connector
def connectToServer(host, user_name, password='',database='practice'):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user_name,
            passwd=password,
            database=database
        )
        print("MySQL Database Connection Successfully Established")
    except Exception as err:
        print(f"Error: {err}")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # Commit Method commits the changes by connector to actual sql server
    except Exception as err:
        print(f"Error: {err}")

