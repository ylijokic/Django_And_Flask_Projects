import sys
# for declaring the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base
# for creating foreign key relationships
from sqlalchemy.orm import relationship
# for configuration
from sqlalchemy import create_engine

# Instance of declarative_base
Base = declarative_base()

# Create Classes
class Venue(Base):
    __tablename__ = 'venue'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)


class Team(Base):
    __tablename__ = 'team'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # home_venue_id = Column(Integer, ForeignKey('venue.id'))


engine = create_engine('sqlite:///pinball-league.db')

Base.metadata.create_all(engine)