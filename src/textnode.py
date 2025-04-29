from enum import Enum

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