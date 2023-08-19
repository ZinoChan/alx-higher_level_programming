#!/usr/bin/python3
"""
Lists States from db
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        	.format(username, password, database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == (searched,))
    try:
        print(state[0].id)
    except IndexError:
        print("Not found")
