from jinja2 import Template
index_html = open("content/index.html").read()
template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
title="Homepage",
content=index_html,
)