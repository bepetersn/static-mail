
subject: 

    The next cool service at {{ promo.percent_off }}% off!

text:

    Hey {{ contact.full_name }}, try out our service by visiting:
    https://coolservice.com/. You could get {{ promo.percent_off }}% off
    if you start soon! This message is short to encourage you to read your
    emails in HTML.

html: 

    {% extends '_base.html' %}
    {% block content %}
    {% block title %} Use Our Cool Service {% endblock %}
    <h3>Have you ever wanted to use a cool service? </h3>
      <p>
        Hey {{ contact.full_name }}, try out ours today by visiting:
        https://coolservice.com/'. Start before {{ promo.end_date }}, and you can
        use promo code {{ promo.code }} to get {{ promo.percent_off }}% off!
      </p>
    {% endblock %}
