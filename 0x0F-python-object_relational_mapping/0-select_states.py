#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Parse command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create cursor object
        cursor = db.cursor()

        # Execute SQL query to select all states from the states table
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

    except MySQLdb.OperationalError as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

