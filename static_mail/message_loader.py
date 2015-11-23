from contextlib import contextmanager
from jinja2.loaders import DictLoader, ChoiceLoader, FileSystemLoader
from simple_configparser import SimpleConfigParser
from .message_template import MessageTemplate

MESSAGE_DIR = '/home/brian/code/static-mail/examples/good/emails'


class DynamicLoader(ChoiceLoader):

    """
    A subclass of ChoiceLoader that takes a
    directory where templates can be found,
    as well as providing a contextmanager
    for adding a dict of extra string
    templates.

    """

    def __init__(self, search_dir):
        super(DynamicLoader, self).__init__([
            DictLoader({}),
            FileSystemLoader(search_dir)
        ])

    @property
    def extra(self):
        return self.loaders[0].mapping

    @extra.setter
    def extra(self, extra):
        self.loaders[0].mapping = extra

    @contextmanager
    def add_templates(self, templates):
        try:
            self.extra = templates
            yield self
        finally:
            self.extra = {}


class MessageLoader(DynamicLoader):

    """
    A loader which overrides the `load` method
    to do special parsing for templates ending
    in '.msg'.

    If one of these files is found, returns the
    resulting MessageTemplate.

    """

    def load(self, environment, name, globals=None):

        if not name.endswith('.msg'):
            return super(MessageLoader, self).load(environment, name, globals)
        else:

            parser = SimpleConfigParser()
            with open(MESSAGE_DIR + name) as f:
                parser.read_file(f)

            return MessageTemplate(environment, parser.items())

