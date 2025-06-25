from textnode import TextNode,TextType
from shutil import *
from markdown_blocks import *
from htmlnode import *
import os
def main():
   print(extract_title("# Title"))
   copy_to_dir("static","public")
   generate_pages_recursive("content", "template.html", "public")

def copy_to_dir(source, destination):
   clear_directory(destination)
   if os.path.isdir(source) == True:
      copy_items(source,os.listdir(source),destination)

def copy_items(source, items, destination):
   for item in items:
      if os.path.isdir(f"{source}/{item}"):
         os.mkdir(f"{destination}/{item}")
         copy_items(f"{source}/{item}",os.listdir(f"{source}/{item}"), f"{destination}/{item}")
      if os.path.isfile(f"{source}/{item}") == True:
         copy(f"{source}/{item}",destination)

def clear_directory(destination):
   print(os.path.isdir(destination))
   if os.path.isdir(destination) == True:
      rmtree(destination)
   os.mkdir(destination)

def extract_title(markdown):
   lines = []
   lines = markdown.split("\n")
   for line in lines:
      if line.startswith("# "):
         return line[2:]
   raise Error("No title found")

def generate_page(from_path, template_path, dest_path):
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   print(os.path.isfile(from_path))
   with open(from_path, "rt") as f:
      markdown = f.read()
   with open(template_path, "rt") as f:
      template = f.read()
   HTMLnode = markdown_to_html_node(markdown)
   HTML_string = HTMLnode.to_html()
   print(HTMLnode)
   print(HTML_string)
   title = extract_title(markdown)
   print(template)
   template = template.replace("{{ Title }}",title)
   template = template.replace("{{ Content }}", HTML_string)
   print(template)
   with open(dest_path, "w") as f:
      f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   content = os.listdir(dir_path_content)
   for item in content:
      if os.path.isfile(os.path.join(dir_path_content, item)):
         if item.endswith(".md"):
            dest_name = item.replace(".md", ".html")
            generate_page(os.path.join(dir_path_content,item),template_path, os.path.join(dest_dir_path, dest_name))
      if os.path.isdir(os.path.join(dir_path_content, item)):
         os.makedirs(os.path.join(dest_dir_path, item), exist_ok=True)
         generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))

if __name__ == "__main__":
    main()