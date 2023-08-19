#!/usr/bin/python3
"""
Lists States from db
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(State, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print(city[0] + ": (" + str(city[1]) + ") " + city[2])
