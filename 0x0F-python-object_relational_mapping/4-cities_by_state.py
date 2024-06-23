#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_0_usa"""


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

        # Query
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )

        # Execute query
        cursor.execute(query)

        # Fetch all rows returned by the query
        cities = cursor.fetchall()

        # Print the fetched states
        for city in cities:
            print(city)

        # Close the cursor and database connection
        cursor.close()
        db.close()
