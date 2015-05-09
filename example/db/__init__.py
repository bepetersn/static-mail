
from __future__ import unicode_literals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Get connection to a database
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()

# Create database schemas
Base.metadata.create_all(engine)


