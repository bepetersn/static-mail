

class StaticMail(object):

    def __init__(self, config_object):
        print("Got mail server config info: ")
        print(config_object.__config_store__)

    def send_email_by_name(self, name, recipients, context=None):
        print name
        print recipients
        print context
        return self
