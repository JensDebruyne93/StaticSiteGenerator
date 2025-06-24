from textnode import TextNode,TextType
from os import *
from shutil import *
def main():
   dummy = TextNode("This is some anchor text", TextType.LINK , "https://www.boot.dev")
   print(repr(dummy))
   copy_to_dir("static","public")

def copy_to_dir(source, destination):
   clear_directory(destination)
   if path.isdir(source) == True:
      copy_items(source,listdir(source),destination)

def copy_items(source, items, destination):
   for item in items:
      if path.isdir(f"{source}/{item}"):
         mkdir(f"{destination}/{item}")
         copy_items(f"{source}/{item}",listdir(f"{source}/{item}"), f"{destination}/{item}")
      if path.isfile(f"{source}/{item}") == True:
         copy(f"{source}/{item}",destination)

def clear_directory(destination):
   print(path.isdir(destination))
   if path.isdir(destination) == True:
      rmtree(destination)
   mkdir(destination)

if __name__ == "__main__":
    main()