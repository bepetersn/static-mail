
from __future__ import unicode_literals
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Unicode, DateTime

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(40))
    last_name = Column(Unicode(60))
    email = Column(Unicode(254))

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return '<User: {}>'.format(self.full_name)


class Promotion(Base):

    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True)
    flt_percent_off = Column(Float)
    start_dt = Column(DateTime)
    end_dt = Column(DateTime)

    @property
    def percent_off(self):
        return '{0:.0f}'.format(self.flt_percent_off * 100)

    @property
    def end_date(self):
        return self.end_dt.strftime('%b %d')

    def __repr__(self):
        return '<Promo: {}% off until {}>'.format(self.percent_off, self.end_date)
