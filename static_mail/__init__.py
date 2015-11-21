import unittest.mock as mock
from .message_loader import MessageLoader
from simple_mail import Mail

class StaticMail(object):

    def __init__(self, config, logger=None):
        """
        Store config for the mail server, and the location 
        of email templates.

        """

        self.config = config
        self.mail = Mail(config)
        self.logger = logger if logger is not None else mock.Mock()

    def send_email_by_name(self, name, recipients, context=None):
        """
            1) Build the email template of `name`, as found
            under the emails directory, with the given
            context--where that directory is should be
            configurable.
            2) Load the subject and text for the given template
            name, as defined in <EMAIL_DIR>/use_my_service.msg. Each is
            turned into a template and built with the given
            context as well.

        """

        message = MessageLoader.get_message(name)
        message.render(**context)
        self.mail.reply(recipients, **message)