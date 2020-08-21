import mysql.connector

try: 
    token = os.getenv("TOKEN")
    HOST = os.getenv ("HOST")
    USER = os.getenv ("USER")
    PASSWORD = os.getenv ("PASSWORD")
    DATABASE = os.getenv ("DATABASE")

    connection = mysql.connector.connect (
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
        )
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")