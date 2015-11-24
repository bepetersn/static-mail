
from unittest import TestCase, mock
from jinja2 import TemplateNotFound
from static_mail import DynamicLoader


class TestDynamicLoader(TestCase):

    TEMPLATES = {
        'greeting': 'Hello {{ user.name }}! Hope you and {{ pet.name }} have a good day.',
        'valediction': 'See you later! Please order from us again at {{ location.name }}.'
    }

    def test_templates_added_are_available_in_context(self):

        loader = DynamicLoader('/path/not/under/test')

        self.assertRaises(TemplateNotFound, loader.get_source,
                          mock.Mock(), 'greeting')

        with loader.add_templates(self.TEMPLATES):
            self.assertEqual(self.TEMPLATES['greeting'], loader.get_source(mock.Mock(), 'greeting')[0])

        self.assertRaises(TemplateNotFound, loader.get_source,
                          mock.Mock(), 'greeting')
