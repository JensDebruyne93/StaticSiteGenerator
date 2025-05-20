from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value == None or len(value) == 0:
            raise ValueError("All LeafNodes must have a value.")
        super().__init__(tag, value,[],props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All LeafNodes must have a value.")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"