from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://gov-track@localhost/gov-track')

from tables import Base
# Create tables if they don't exist.
Base.metadata.create_all(engine)
# Create a base session for interaction.
interface = sessionmaker(bind=engine)
