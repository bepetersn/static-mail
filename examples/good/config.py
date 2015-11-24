
from confyg import JsonConfyg
from simple_mail import DefaultConfig
import os


class FileConfig(JsonConfyg):

    __source__ = '/etc/dev/mail-config.json'

    EMAIL_ADDRESS = 'email-address'
    EMAIL_PASSWORD = 'email-password'


# Confyg loads these values from a JSON file at __source__,
# see their docs: http://confyg.readthedocs.org/en/latest/.
FileConfig.load()


class ExampleConfig(DefaultConfig, FileConfig):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    HOST_STRING = '{}:{}'.format(MAIL_SERVER, MAIL_PORT)
    NAME = 'Brian Peterson'
    REPLY_TO = FileConfig.EMAIL_ADDRESS
    BASE_DIR = os.path.dirname(__file__)
    MESSAGE_DIR = os.path.join(BASE_DIR, 'emails')
