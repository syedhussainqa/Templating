import glob
import os
from jinja2 import Template



all_html_files = glob.glob("content/*.html")
pages = []
base_file = "templates/base.html"

# for each_html_file in all_html_files:

#     file_path = each_html_file
#     file_name = os.path.basename(file_path)
#     name_only, extension = os.path.splitext(file_name)
#     return pages.append({
#     "filename": file_path,
#     "title": name_only,
#     "output": "docs/" + file_name,
#     })

# def read_content_html(pages):
#     read_file = open(page['filename']).read()
#     return read_file


# def merge_base_template(pages, base_file):
#     base_html = open(base_file).read()
#     template = Template(base_html)
#     final_template = template.render(
#         title=page['title'],
#         content= index_html,
#     )
#     return final_template

# def write_to_final_html(final_template):
#     output_pages = open(page["output"] , "w+").write(final_template)
#     return output_pages

# def main():
#     read_content_html()
#     merge_base_template()
#     write_to_final_html()


#loop through each html file 
for each_html_file in all_html_files:

    file_path = each_html_file
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    pages.append({
    "filename": file_path,
    "title": name_only,
    "output": "docs/" + file_name,
    })



for page in pages:
    index_html = open(page['filename']).read()
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    final_template = template.render(
        title=page['title'],
        content= index_html,
    )
    open(page["output"] , "w+").write(final_template)
    print('Pages are created')

