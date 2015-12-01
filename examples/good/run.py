#!/usr/bin/env python

from __future__ import unicode_literals

from db import session
from db.models import User, Promotion
from db.bootstrap import bootstrap_data
from config import ExampleConfig
from templated_mail import TemplatedMail


if __name__ == '__main__':

    # do init
    config = ExampleConfig()
    mail = TemplatedMail(config)
    bootstrap_data()

    # act like we know why we're emailing people
    user = session.query(User).first()
    new_promo = session.query(Promotion).first()

    mail.send_message(
        name='use_my_service',
        recipients=[user.email],
        context={
            'contact': user,
            'promo': new_promo
        }
    )
