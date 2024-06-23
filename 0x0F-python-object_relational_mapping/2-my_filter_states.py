#!/usr/bin/python3
"""Script that takes in an argumentand displays all values in the
  states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb
if __name__ == "__main__":
    # Main
    if len(sys.argv) >= 5:
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
        query = (
            "SELECT * FROM states WHERE name LIKE BINARY '{}' "
            "ORDER BY id ASC".format(sys.argv[4])
        )

        # Execute query
        cursor.execute(query)

        # Fetch all rows returned by the query
        states = cursor.fetchall()

        # Print the fetched states
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()
