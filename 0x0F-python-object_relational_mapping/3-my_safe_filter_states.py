#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Construct the query with parameters to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the SQL query with the state name as a paramater
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Displays the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
