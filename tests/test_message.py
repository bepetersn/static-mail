
from unittest import TestCase
from unittest.mock import Mock, MagicMock
from jinja2 import Template
from templated_mail.message import Message


TEMPLATES = {
    'subject': 'Happy Thanksgiving, {{ user.name }}',
    'body': 'Hello {{ user.name }}! Hope you and {{ pet.name }} have a good day.',
    'html': 'See you later! Please order from us again at {{ location.name }}.'
}


class TestMessageTemplate(TestCase):

    def test_message_requires_all_three_sub_templates(self):
        templates = TEMPLATES.copy()
        templates.pop('subject')
        self.assertRaises(AssertionError, Message, Mock(), templates)

    def test_message_successfully_renders(self):

        env = MagicMock(get_template=lambda name: Template(TEMPLATES[name]))
        message = Message(env, TEMPLATES)
        data = message.render(
            user=Mock(name='Brian'),
            pet=Mock(name='Horsey'),
            location= Mock(name='New Wave')
        )
        self.assertIn('Brian', data.subject)
        self.assertIn('Horsey', data.body)
        self.assertIn('New Wave', data.html)
