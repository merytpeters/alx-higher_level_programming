#!/usr/bin/python3
"""Lists out all City objects from the database"""


import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City

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
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for cities
    cities = session.query(City).order_by(City.id).all()

    # Add the new state to the session
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()
