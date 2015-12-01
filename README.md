
# Templated-Mail

### Why This Project

This project provides a simple interface for sending an email while keeping the email's definition
--its text, subject, and html--out of the application logic as much as possible. The following code
is taken from `examples/bad`, and represents what this package is intended to prevent:


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

Yuck. And it really only gets worse from there as your code becomes more complex. Let's try that again, but instead imagine an API that we
would actually like to use. From `examples/good`:

```python

mail.send_message(
    name='use_my_service',
    recipients=[contact.email],
    context={
        'contact': contact,
        'promo': new_promo
    }
)

```

### Defining message templates

All in all, this project makes the assumption that an email's subject, text, and html all may need templating, and can be bundled as text assets. So where is the email? Taking a look in the
`emails/use_my_service.msg` file, we have the beginning of an answer:

```
subject:

    The next cool service at {{ promo.percent_off }}!

body:

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
```

The name we provided is referencing a file with a `.msg` extension. It is associated with a subject, fallback body for if the HTML doesn't display, and the HTML email itself. Notice the templating language at use: this is [Jinja2](http://jinja.pocoo.org/)'s syntax. The values we passed in earlier as `context` get dynamically evaluated for each of these items.

The logic of `send_message` is simple. It looks in the `MESSAGE_DIR`, defined in the configuration object, for files ending in `.msg`. The `subject`, `body`, and `HTML` templates are taken from this file, and are all evaluated
with the same context. The templates support all of Jinja2's features, up to and including inheritance.

### Keeping Your HTML Separate

Let's say you want a base template. Put it in the same directory as the emails, and it will be found. If you want to define your HTML in its own separate file for any reason (syntax, etc.), you can easily do so. Just write an HTML section in the .msg file that `extends` your HTML.

```
    html:

      {% extends 'use_my_service.html' %}

```

In case you were wondering, the syntax of the `.msg` files is the same as that of a .INI style file, minus the need for sections. Keep in mind that lines that start a new key-value pair can't have any whitespace before the key. Other than that, go crazy with it.


### Future

I was thinking of adding support for a `markdown` key to support that format, or possibly others, besides `subject`, `body`, and `text`. I also was
considering dropping the need for `body` at all, if you don't want it.
