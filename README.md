
# Why This Project

This project provides a simple interface for sending an email while keeping the email's definition--its text, subject, and html--out of the application logic as much as possible. The following code is roughly taken from `examples/good`:

```python

# do init
class MailConfig(object):
  MAIL_USERNAME = 'me@myserver.com'
  MAIL_PASSWORD = 'mypassword'

mail = StaticMail(MailConfig())

# act like we know why we're emailing people
contact = session.query(Contact).first()
new_promo = session.query(Promotion).first()

# send an email
mail.send_email_by_name(
    name='use_my_service',
    recipients=[contact.email],
    context={
        'contact': contact,
        'promo': new_promo
    }
)

```

So where is the email? All we've provided is a name. Taking a look in the `emails.yaml` file, we have part of the answer:

```yaml

-  use_my_service:
    subject: 'The next cool service at {{ promo.percent_off }}!'
    plain_text: 'Hey {{ contact.full_name }}, try out our service by visiting:
    https://coolservice.com/. You could get {{ promo.percent_off }}% off
    if you start soon! This message is short to encourage you to read your
    emails in HTML.'

```

Here the name we provided is associated with a subject and fallback text for if the HTML doesn't display. Notice the templating language at use: this is [Jinja2](http://jinja.pocoo.org/)'s syntax. The values we passed in earlier as `context` get dynamically evaluated for each of these items.

Finally, under `emails/use_my_serice.html` we have the email template itself:


```html

{% extends 'emails/_base.html' %}

{% block content %}
{% block title %} Use Our Cool Service {% endblock %}
    <h3>Have you ever wanted to use a cool service? </h3>
    <p>
      Hey {{ contact.full_name }}, try out ours today by visiting:
      https://coolservice.com/'. Start before {{ promo.end_date }}, and you can
      use promo code {{ promo.code }} to get {{ promo.percent_off }}% off!
    </p>
{% endblock %}

```

Again, we're relying on Jinja. The logic of `send_email_by_name` is very simple. The HTML template is evaluated with the same context as the `subject` and `plain_text` were.

Overall, this project makes the assumption that in sending emails programmatically, the subject, text, and html all *go together*, and thus there's no reason not to bundle this data and reference it as one item, in our case by the name of the email template.
