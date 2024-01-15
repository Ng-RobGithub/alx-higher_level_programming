#!/usr/bin/python3
""" lists the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    """ Set up connection to the database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """ Bind the database """
    Base.metadata.create_all(engine)

    """ Create a session to interact with the database """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query to retrieve all City objects """
    for instance in session.query(State).order_by(State.id):
        """ Display the results """
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)
