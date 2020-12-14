#!/usr/bin/python3
"""State Model"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ not executed when imported """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    store = session.query(City, State).filter(City.state_id == State.id)
    for i in store:
        print("{}: ({}) {}".format(i.State.name, i.City.id,
                                   i.City.name))
    session.close()
