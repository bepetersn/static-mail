
from __future__ import unicode_literals
from datetime import datetime, timedelta
from db import session
from db.models import User, Promotion

def bootstrap_data():

    # Make some data
    u = User(
        first_name='Brian',
        last_name='Peterson',
        email='bepetersn@gmail.com'
    )
    p = Promotion(
        flt_percent_off=.5,
        start_dt=datetime.utcnow(),
        end_dt=datetime.utcnow() + timedelta(days=5),
    )
    session.add_all([u, p])
    session.commit()
