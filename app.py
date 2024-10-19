import mysql.connector
from mysql.connector import Error

# Creating a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       
            user="root",            
            password="Rohini@986",    
            database="rohinidb"  
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None
    
# Create (INSERT) Operation
def create_registration(connection, name, email, dob, phone_number):
    cursor = connection.cursor()
    sql = "INSERT INTO Registration (Name, Email, DOB, PhoneNumber) VALUES (%s, %s, %s, %s)"
    values = (name, email, dob, phone_number)

    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Registration created successfully!")
    except mysql.connector.Error as error:
        print(f"Failed to insert record: {error}")
    finally:
        cursor.close()

# Read (SELECT) Operation
def get_registration_by_id(connection, id):
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM Registration WHERE ID = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("No record found with that ID.")
    
    cursor.close()

# Update (UPDATE) Operation
def update_registration(connection, id, name=None, email=None, dob=None, phone_number=None):
    cursor = connection.cursor()
    updates = []
    values = []

    if name:
        updates.append("Name = %s")
        values.append(name)
    if email:
        updates.append("Email = %s")
        values.append(email)
    if dob:
        updates.append("DOB = %s")
        values.append(dob)
    if phone_number:
        updates.append("PhoneNumber = %s")
        values.append(phone_number)
    
    values.append(id)

    sql = f"UPDATE Registration SET {', '.join(updates)} WHERE ID = %s"
    
    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Registration updated successfully!")
    except mysql.connector.Error as error:
        print(f"Failed to update record: {error}")
    finally:
        cursor.close()

# Delete (DELETE) Operation
def delete_registration(connection, id):
    cursor = connection.cursor()
    sql = "DELETE FROM Registration WHERE ID = %s"

    try:
        cursor.execute(sql, (id,))
        connection.commit()
        print("Registration deleted successfully!")
    except mysql.connector.Error as error:
        print(f"Failed to delete record: {error}")
    finally:
        cursor.close()


if __name__ == "__main__":
    connection = create_connection()

    # Create a new registration
    create_registration(connection, 'John Doe', 'john.doe@example.com', '1990-01-01', '1234567890')

    # Read a registration by ID
    get_registration_by_id(connection, 1)

    # Update a registration
    update_registration(connection, 1, name="Jane Doe", email="jane.doe@example.com")

    # Delete a registration
    delete_registration(connection, 1)

