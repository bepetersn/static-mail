#!/usr/bin/env python

from __future__ import unicode_literals
from db import session
from db.models import User, Promotion
from db.bootstrap import bootstrap_data
from config import MailConfig
from static_mail import StaticMail


if __name__ == '__main__':

    # do init
    config = MailConfig()
    mail = StaticMail(config)

    # create bootstrap data
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


