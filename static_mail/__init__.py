import simple_mail as mail
import unittest.mock as mock
from .environment import MessageEnvironment
from .loader import DynamicLoader
from .template import MessageTemplate


class StaticMail(object):

    def __init__(self, config, logger=None):
        """
        Store config for the mail server, and the location 
        of email templates.

        """

        self.config = config
        self.mail = mail.Mail(config)
        self.env = MessageEnvironment(loader=DynamicLoader(
            self.config.TEMPLATE_DIR
        ))
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

        template = self.env.get_template('{}.msg'.format(name))
        self.mail.reply(recipients, **template.render(**context))