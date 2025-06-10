from textnode import TextNode, text_node_to_html_node, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
        else: 
            split_node = node.text.split(delimiter)
            for i in range(0,len(split_node)):
                if i%2 != 0:
                    new_nodes.append(TextNode(split_node[i],text_type))
                elif len(split_node[i])>0:
                    new_nodes.append(TextNode(split_node[i],TextType.NORMAL_TEXT))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
            if node.text_type != TextType.NORMAL_TEXT:
                new_nodes.append(node)
            else:
                image_markdown = extract_markdown_images(node.text)
                if image_markdown != None and len(image_markdown) > 0:
                    split_nodes = node.text.split(f"![{image_markdown[0][0]}]({image_markdown[0][1]})")
                    if len(split_nodes) == 1:
                        new_nodes.append(TextNode(image_markdown[0][0],TextType.IMAGE, image_markdown[0][1]))
                    else:
                        if len(split_nodes[0]) > 0:
                            new_nodes.append(TextNode(split_nodes[0],TextType.NORMAL_TEXT))
                        new_nodes.append(TextNode(image_markdown[0][0],TextType.IMAGE, image_markdown[0][1]))
                        if len(split_nodes[1]) > 0:
                            new_nodes.extend(split_nodes_image([TextNode(split_nodes[1],TextType.NORMAL_TEXT)]))
                else:
                    new_nodes.append(node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
            if node.text_type != TextType.NORMAL_TEXT:
                new_nodes.append(node)
            else:
                link_markdown = extract_markdown_links(node.text)
                if link_markdown != None and len(link_markdown) > 0:
                    split_nodes = node.text.split(f"[{link_markdown[0][0]}]({link_markdown[0][1]})")
                    if len(split_nodes) == 1:
                        new_nodes.append(TextNode(link_markdown[0][0],TextType.LINK, link_markdown[0][1]))
                    else:
                        if len(split_nodes[0]) > 0:
                            new_nodes.append(TextNode(split_nodes[0],TextType.NORMAL_TEXT))
                        new_nodes.append(TextNode(link_markdown[0][0],TextType.LINK, link_markdown[0][1]))
                        if len(split_nodes[1]) > 0:
                            new_nodes.extend(split_nodes_link([TextNode(split_nodes[1],TextType.NORMAL_TEXT)]))
                else:
                    new_nodes.append(node)
    return new_nodes