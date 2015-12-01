
subject: 

    The next cool service at {{ promo.percent_off }}% off!

body:

    Hey {{ contact.full_name }}, try out our service by visiting:
    https://coolservice.com/. You could get {{ promo.percent_off }}% off
    if you start soon! This message is short to encourage you to read your
    emails in HTML.

html: 

    {% extends 'use_my_service.html' %}
