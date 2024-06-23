#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb
if __name__ == "__main__":
    # Main
    if len(sys.argv) == 4:
        # Connection to a MySQL server database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )

        # Object to interact with the database
        cursor = db.cursor()

        # Execute the query to list all states
        cursor.execute(
            "SELECT * FROM states WHERE name "
            "LIKE 'N%' ORDER BY id ASC"
        )

        # Fetch all rows returned by the query
        states = cursor.fetchall()

        # Print the fetched states
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()
