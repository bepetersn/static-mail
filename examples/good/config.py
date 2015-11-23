
from confyg import JsonConfyg


class FileConfig(JsonConfyg):

    __source__ = '/etc/dev/mail-config.json'

    MAIL_USERNAME = 'mail-username'
    MAIL_PASSWORD = 'mail-password'


# Confyg loads these values from a JSON file at __source__,
# see their docs: http://confyg.readthedocs.org/en/latest/.
FileConfig.load()


class Config(FileConfig):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    DEFAULT_MAIL_SENDER = FileConfig.MAIL_USERNAME
    
    BASE_DIR = os.path.dirname(__file__)
    MESSAGE_DIR = os.path.join(BASE_DIR, 'emails')
