
from simple_templating import Templating
from . import config

t = Templating.from_dir(config.TEMPLATE_DIR)


class MessageLoader:
    pass