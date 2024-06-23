#!/usr/bin/python3
"""Prints id of state passed as argument"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        # Number of arguments specified
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_to_search = sys.argv[4]

    # Create engine and connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, database_name)
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query state entereas argument
    state = (
        session.query(State)
        .filter(State.name == state_to_search)
        .first()
    )

    # Print the id of fetched states
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
