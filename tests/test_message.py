
from unittest import TestCase
from unittest.mock import Mock
from jinja2 import Environment
from templated_mail import SubTemplateLoader
from templated_mail.message import Message


class TestMessageTemplate(TestCase):

    TEMPLATES = {
        'subject': 'Happy Thanksgiving, {{ user.name }}',
        'body': 'Hello {{ user.name }}! Hope you and {{ pet.name }} have a good day.',
        'html': 'See you later! Please order from us again at {{ location.name }}.'
    }

    def test_message_requires_all_three_sub_templates(self):
        templates = self.TEMPLATES.copy()
        templates.pop('subject')
        self.assertRaises(AssertionError, Message, Mock(), templates)

    def test_message_successfully_renders(self):
        message = Message(Environment(loader=SubTemplateLoader('/not/under/test')),
                          self.TEMPLATES)
        data = message.render(
            user=Mock(name='Brian'),
            pet=Mock(name='Horsey'),
            location= Mock(name='New Wave')
        )
        self.assertIn('Brian', data.subject)
        self.assertIn('Horsey', data.body)
        self.assertIn('New Wave', data.html)
