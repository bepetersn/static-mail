#!/usr/bin/env python

from __future__ import unicode_literals

from db import session
from db.models import User, Promotion
from db.bootstrap import bootstrap_data
from templating import render_template
from config import MailConfig
from static_mail import StaticMail


if __name__ == '__main__':

    # do init
    config = MailConfig()
    mail = StaticMail(config)
    bootstrap_data()

    # act like we know why we're emailing people
    user = session.query(User).first()
    new_promo = session.query(Promotion).first()

    mail.reply(
        to=[user.email],
        subject='The next cool service at {}% off!'.format(promo_percent_off=new_promo.percent_off),
        text=('Hey {}, try out our service by visiting: '
                    'https://coolservice.com/. You could get {}'
                    '% off if you start soon! This message is short to encourage '
                    'you to read your emails in HTML.').format(
                        user.full_name,
                        new_promo.percent_off
                    ),
        html=render_template('use_my_service.msg', contact=user, promo=new_promo)
    )
