from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from Inline_markdown import text_to_textnodes
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST ="ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = []
    HTMLnodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        HTMLnodes.append(block_to_html(block_type,block))
    return ParentNode("div", HTMLnodes)
        
def block_to_html(block_type, text):
    blocknode
    childrenNodes = []
    if block_type == BlockType.HEADING:
        number = get_number_of_hashes(text)
    text = clean_text(block_type,text)
    match block_type:
        case BlockType.HEADING:
            childrenNodes = text_to_children(text)
            blocknode = ParentNode(f"h{number}", childrenNodes)
        case BlockType.PARAGRAPH:
            childrenNodes = text_to_children(text)
            blocknode = ParentNode("p", childrenNodes)
        case BlockType.QUOTE:
            childrenNodes = text_to_children(text)
            blocknode = ParentNode("blockquote", childrenNodes)
        case BlockType.ORDERED_LIST:
            listitemChildren = []
            lines = text.split("\n")
            for line in lines:
                listitemChildren = text_to_children(line)
                childrenNodes.append(ParentNode("li", listitemChildren))
            blocknode = ParentNode("ol", childrenNodes)
        case BlockType.UNORDERED_LIST:
            listitemChildren = []
            lines = text.split("\n")
            for line in lines:
                listitemChildren = text_to_children(line)
                childrenNodes.append(ParentNode("li", listitemChildren))
            blocknode = ParentNode("ul", childrenNodes)
        case BlockType.CODE:
            codeNode = TextNode(text,TextType.NORMAL_TEXT)
            codeChild = []
            codeChild.append(text_node_to_html_node(codeNode))
            childrenNodes.append(ParentNode("code", codeChild))               
            blocknode = ParentNode("pre", childrenNodes)
        case _:
            raise ValueError("Not a valid BlockType.")
    return blocknode
        
def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children
        
def clean_text(text, block_type):
    split_text = []
    split_text = text.split("\n")
    match block_type:
            case BlockType.HEADING:
                return text[(get_number_of_hashes(text)+1):]
            case BlockType.PARAGRAPH:
                return text
            case BlockType.QUOTE:
                lines =[]
                for line in split_text:
                    lines.append(line[2:])
                return "\n".join(lines)
            case BlockType.ORDERED_LIST:
                lines =[]
                for line in split_text:
                    line_text = line.split(". ")
                    line_text = ". ".join(line_text[1:])
                    lines.append(line_text)
                return "\n".join(lines)
            case BlockType.UNORDERED_LIST:
                lines =[]
                for line in split_text:
                    lines.append(line[2:])
                return "\n".join(lines)
            case BlockType.CODE:
                return text
            case _:
                raise ValueError("Not a valid BlockType.")

def get_number_of_hashes(text):
    words = []
    words = text.split(" ")
    headerhashes = words[0]
    number_of_hashes = len(headerhashes)   
    return number_of_hashes
