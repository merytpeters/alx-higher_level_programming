#!/usr/bin/python3
"""Prints all Cities and state objects from database"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # Number of arguments specified
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

    # Create engine and connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, database_name)
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Queries for cities and states
    cities = session.query(City).order_by(City.id).all()

    # Print the fetched states and cities
    for city in cities:
        states = session.query(State)\
                        .filter(State.id == city.state_id)\
                        .first().name
        print("{}: ({}) {}".format(states, city.id, city.name))

    # Close session
    session.close()
