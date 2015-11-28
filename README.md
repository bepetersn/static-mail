
# Why This Project

This project provides a simple interface for sending an email while keeping the email's definition
--its text, subject, and html--out of the application logic as much as possible. The following code
is taken from `examples/bad`, and represents what this package is intended to prevent. This kind of
code is commonplace, in the author's experience:


```python

mail.send_message(
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
```

Yuck. Let's try that again, but instead imagine an API that we would actually like to use.

```python

mail.send_email_by_name(
    name='use_my_service',
    recipients=[contact.email],
    context={
        'contact': contact,
        'promo': new_promo
    }
)

```

So where is the email? All we've provided is a name. Taking a look in the
`emails/use_my_service.msg` file, we have the answer:

```
subject:

    The next cool service at {{ promo.percent_off }}!

body:

    Hey {{ contact.full_name }}, try out our service by visiting:
    https://coolservice.com/. You could get {{ promo.percent_off }}% off
    if you start soon! This message is short to encourage you to read your
    emails in HTML.

html:

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

Here the name we provided is associated with a subject, fallback text for if the HTML doesn't
display, and the HTML email itself. Notice the templating language at use: this is
[Jinja2](http://jinja.pocoo.org/)'s syntax. The values we passed in earlier as `context` get
dynamically evaluated for each of these items.

The logic of `send_email_by_name` is simple. It looks in the `MESSAGE_DIR`, defined in the configuration object, for files ending in `.msg`. The `subject`, `body`, and `HTML` templates
are taken from this file, and are all evaluated with the same context.

Overall, this project makes the assumption that in sending emails programmatically,
the subject, body, and html all *go together*, and thus there's no reason not to bundle
this data and reference it as one item, in our case by the name of the email template.
