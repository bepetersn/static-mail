
from simple_mail import DefaultConfig
import os


class ExampleConfig(DefaultConfig):
    EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
    EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    HOST_STRING = '{}:{}'.format(MAIL_SERVER, MAIL_PORT)
    NAME = 'Brian Peterson'
    REPLY_TO = EMAIL_ADDRESS
    BASE_DIR = os.path.dirname(__file__)
    MESSAGE_DIR = os.path.join(BASE_DIR, 'emails')
