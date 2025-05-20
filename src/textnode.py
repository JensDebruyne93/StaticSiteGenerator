from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal text"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text,textType, link=None):
        self.text = text
        self.text_type = TextType(textType)
        if link == "":
            self.URL = None
        else : self.URL = link
    def __eq__(self,textNode):
        textNode = textNode
        if self.text_type == textNode.text_type and self.text == textNode.text and self.URL == textNode.URL:
            return True
        else: return False

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.URL})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i",text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            props = dict(href= text_node.URL)
            return LeafNode("a",text_node.text,props)
        case TextType.IMAGE:
            props = dict(src= text_node.URL, alt = text_node.text)
            return LeafNode("img","",props)
        case _: raise ValueError("Not a valid TextType.")