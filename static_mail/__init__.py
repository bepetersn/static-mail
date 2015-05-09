

class StaticMail(object):

    def __init__(self, config_object):
        pass

    def send_email_by_name(self, name, recipients, context=None):
        print name
        print recipients
        print context
        return self