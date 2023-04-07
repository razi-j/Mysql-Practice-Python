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

def addToTable():
    global query
    try:
        studentID = int(input("Student ID Number: "))
        name=input("Name: ")
        grade=int(input("Grade Level (1, 2, etc.): "))
        query=f"""
        INSERT INTO data VALUES({studentID}, '{name}', {grade});
        """
    except Exception as err:
        print(f"ERror: {err}")
    
    return query

db = connectToServer("localhost", "root")

#create_table= """
#create table data (
#student_ID INT PRIMARY KEY,
#Name VARCHAR(50),
#Grade INT,
#Passing BOOLEAN
#);
#"""

student=addToTable()
execute_query(db, student)

