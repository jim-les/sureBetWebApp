import mysql.connector

def check_database_exists(hostname, username, password, database_name):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password
        )
        
        # Create a cursor object to execute queries
        cursor = connection.cursor()
        
        # Execute a query to check if the database exists
        query = f"SHOW DATABASES LIKE '{database_name}'"
        cursor.execute(query)
        
        # Fetch the result of the query
        result = cursor.fetchone()
        
        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # If result is not None, the database exists
        return result is not None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Example usage
hostname = 'localhost'
username = 'mypense3_surebetAdmin'
password = 'surebetadminpassword'
database_name = 'mypense3_sureBetDjangoDatabase'

if check_database_exists(hostname, username, password, database_name):
    print(f"The database '{database_name}' exists.")
else:
    print(f"The database '{database_name}' does not exist.")

