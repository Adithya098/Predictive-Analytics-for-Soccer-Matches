import sqlite3

def list_tables(database_path):
    """List all tables in the specified SQLite database.
    
    Args:
    database_path (str): Path to the SQLite database file.
    
    Returns:
    list: A list of table names.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Retrieve all the table names using the SELECT statement on sqlite_master
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    # Fetch all results from the executed SQL command
    tables = cursor.fetchall()
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    # Return the list of tables
    return [table[0] for table in tables]  # Unpacking the result tuples

# Example usage
database_path = 'my_database.db'  # Provide the path to your SQLite database file
tables = list_tables(database_path)
print("Tables in the database:", tables)
