

class StaticMail(object):

    def __init__(self, config_object):
        """
        Store config for the mail server, the location of email
        templates, the location of the `emails.yaml` file, etc.

        """

        print("Got config info: ")
        print(config_object.__config_store__)

    def send_email_by_name(self, name, recipients, context=None):
        """
            1) Build the email template of `name`, as found
            under the emails directory, with the given
            context--where that directory is should be
            configurable.
            2) Load the subject and text for the given template
            name, as defined in <EMAIL_DIR>/emails.yaml. Each is
            turned into a template and built with the given
            context as well.

        """

        print('build email with name: {}'.format(name))
        print('use context: {}'.format(context))
        return self

        #subject = self.get_subject_somehow()
        #html = self.get_html_somehow()
        #plain_text = self.get_plain_text_somehow()
        #send_message(recipients, subject, plain_text, html)

    def send_message(self, recipients, subject, plain_text, html):
        """
        The final subject, plain_text, and html are used
        to send an email message. Flask-Mail's Message class
        has a nice interface, we will probably make our
        interface compatible with that to the extent possible.

        """

        print('send to recipients: {}'.format(recipients))
        print('with subject: {}'.format(subject))
        print('with plain_text: {}'.format(plain_text))
        print('with html: {}...'.format(html[:200]))
        return self
