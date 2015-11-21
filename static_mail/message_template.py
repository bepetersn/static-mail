from jinja2 import Template


class MessageTemplate:
    """
    A message_template encapsulates a set of three templates:
        - subject
        - plain_text
        - html

    A message_template can be rendered with a given context.

    """

    TEMPLATES = ('subject', 'plain_text', 'html')

    def __init__(self, subject, plain_text, html):
        self._subject = subject
        self._plain_text = plain_text
        self._html = html

    def get_sub_template(self, name):
        return Template(getattr(self, '_{0}'.format(name)))

    def render(self, **context):
        for template_name in self.TEMPLATES:

            template.render(**context)