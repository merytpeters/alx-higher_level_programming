#!/usr/bin/python3
"""Lists all State objects that contains a"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

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

    # Query states with letter a
    State_a = (
        session.query(State).filter(State.name.like('%a%'))
        .order_by(State.id).all()
    )

    # Print the fetched states
    for state in State_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
