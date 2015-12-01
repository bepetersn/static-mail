from functools import partial
import os
from jinja2 import Environment
from simple_configparser import SimpleConfigParser

from templated_mail.sub_template_loader import SubTemplateLoader
from templated_mail.message import Message


class MessageLoader(object):

    """
    A "loader" (though not a Jinja2 subclass) for
    finding files ending in '.msg' in `config.MESSAGE_DIR`.

    """

    def __init__(self, config):
        self.config = config
        self.search_path = config.MESSAGE_DIR
        self.message_class = partial(Message, Environment(
            loader=SubTemplateLoader(
                config.MESSAGE_DIR
            )
        ))

    def get_message(self, name):
        """

        :param name: Takes the name of a message in config.MESSAGE_DIR,
                     without the '.msg' extension.
        :return:     The corresponding Message if it could be found,
                     otherwise None.
        """

        with open(os.path.join(self.search_path, '{}.msg'.format(name))) as f:
            try:
                parser = SimpleConfigParser()
                parser.read_file(f)
                return self.message_class(parser.items())
            except OSError:
                self.config.logger.error('couldn\'t find the file')
                return None