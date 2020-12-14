#!/usr/bin/python3
"""State Model"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    entry = session.query(State).filter(State.id == 2).first()
    entry.name = "New Mexico"
    session.commit()
    session.close()
