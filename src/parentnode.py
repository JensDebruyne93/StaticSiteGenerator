from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("All ParentNodes should have a tag.")
        if children is None:
            raise ValueError("All ParentNodes should have children.")
        super().__init__(tag, "", children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All ParentNodes should have a tag.")
        if self.children is None:
            raise ValueError("All ParentNodes should have children.")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"