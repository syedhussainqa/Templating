import glob
import os
from jinja2 import Template

all_html_files = glob.glob("content/*.html")
pages = []
for each_html_file in all_html_files:

    file_path = each_html_file
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    pages.append({
    "filename": file_path,
    "title": name_only,
    "output": "docs/" + file_name,
    })
print(pages)

for page in pages:
    index_html = open(page['filename']).read()
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    template.render(
    title=page['title'],
    content= index_html,
    )