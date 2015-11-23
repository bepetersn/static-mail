import bunch

SUB_TEMPLATES = {
    'subject',
    'text',
    'html'
}

class MessageTemplate:

    def __init__(self, env, sub_templates):
        self.sub_templates = sub_templates
        self.env = env

    def render_part(self, name, **context):
        return self.env.get_template(name).render(**context)

    def render(self, **context):
        with self.env.loader.add_templates(self.sub_templates):
            values = bunch.Bunch()
            for name in SUB_TEMPLATES:
                values[name] = self.render_part(name, **context)
            return values
