#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
  lists all cities from the database hbtn_0e_0_usa"""


import sys
import MySQLdb
if __name__ == "__main__":
    # Main
    if len(sys.argv) >= 5:
        # Connection to a MySQL server database
        state_name = sys.argv[4:]

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
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s"
        )

        # Execute query
        cursor.execute(query, (state_name,))

        # Fetch all rows returned by the query
        cities = cursor.fetchall()

        # Print the fetched states
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))

        # Close the cursor and database connection
        cursor.close()
        db.close()
