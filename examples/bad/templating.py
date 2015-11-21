
"""
message_template.py

A small module that provides an interface compatible with Flask's render_template.

"""

from jinja2 import Environment, FileSystemLoader
import os

templates_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'emails')
env = Environment(loader=FileSystemLoader(templates_dir))


def render_template(template_name, **context):
    return env.get_template(template_name).render(**context)