import sqlite3  # Import the sqlite3 module to interact with SQLite databases

# Connect to SQLite database (or create it if it doesn't exist)
# This function call establishes a connection to an SQLite database file named 'example.db'.
# If 'example.db' does not exist, it will be created in the current directory.
conn = sqlite3.connect('example.db')

# Create a cursor object
# A cursor is an object that allows us to interact with the database and execute SQL commands.
cursor = conn.cursor()

# Create a table
# The cursor.execute() method is used to execute SQL commands.
# Here, we are creating a table named 'users' with three columns: 'id', 'name', and 'age'.
# The 'id' column is an INTEGER and will serve as the PRIMARY KEY, which uniquely identifies each record.
# The 'name' column is of type TEXT and cannot be NULL (NOT NULL).
# The 'age' column is also of type INTEGER and cannot be NULL.
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert some data into the table
# We use the cursor.execute() method again to insert data into the 'users' table.
# The SQL command here inserts three records into the 'users' table with the given 'name' and 'age' values.
cursor.execute('''
INSERT INTO users (name, age)
VALUES ('Alice', 30), ('Bob', 24), ('Charlie', 29)
''')

# Commit the transaction
# The conn.commit() method saves (commits) the changes made to the database.
# Without this step, the changes would not be saved, and any data inserted would be lost.
conn.commit()

# Select all data from the table
# Here, we execute a SELECT statement to retrieve all records from the 'users' table.
cursor.execute('SELECT * FROM users')

# Fetch all results from the executed query
# The cursor.fetchall() method fetches all rows of the query result and returns them as a list of tuples.
# Each tuple represents a row in the 'users' table.
rows = cursor.fetchall()

# Print the results
# We use a for loop to iterate through the list of tuples and print each row.
# This displays the content of the 'users' table.
for row in rows:
    print(row)

# Close the connection
# Finally, we close the connection to the database using the conn.close() method.
# This is important to free up resources and ensure that all changes are properly saved.
conn.close()

