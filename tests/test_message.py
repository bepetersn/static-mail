
from unittest import TestCase
from unittest.mock import Mock
from templated_mail.message import Message


class TestMessageTemplate(TestCase):

    TEMPLATES = {
        'body': 'Hello {{ user.name }}! Hope you and {{ pet.name }} have a good day.',
        'html': 'See you later! Please order from us again at {{ location.name }}.'
    }

    def test_message_requires_all_three_sub_templates(self):
        self.assertRaises(AssertionError, Message, Mock(), self.TEMPLATES)
