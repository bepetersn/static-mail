import os
import unittest
import unittest.mock as mock
import simple_configparser

from templated_mail.message_loader import MessageLoader

TMP_DIR = '/tmp'


class TestMessageLoader(unittest.TestCase):

    TEMPLATES = {
        'subject': 'Good day {{ user.name }}!',
        'body': 'Hello {{ user.name }}! Hope you and {{ pet.name }} have a good day.',
        'html': 'See you later! Please order from us again at {{ location.name }}.'
    }

    def _load_message(self, name):
        loader = MessageLoader(mock.Mock(MESSAGE_DIR=TMP_DIR))
        return loader.get_message(name)

    def test_load_a_message(self):

        test_name = 'whatever'
        test_file_name = '{}.msg'.format(test_name)
        test_file_path = os.path.join(TMP_DIR, test_file_name)

        message = self._load_message(test_name)
        self.assertIsNone(message)

        with open(test_file_path, 'w') as f:
            parser = simple_configparser.SimpleConfigParser(defaults=self.TEMPLATES)
            parser.write(f)

        message = self._load_message(test_name)
        self.assertIsNotNone(message)
        self.assertEqual(message.sub_templates, self.TEMPLATES)

        os.remove(test_file_path)

        message = self._load_message(test_name)
        self.assertIsNone(message)
