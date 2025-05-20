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
        children_html = map(lambda x=self : children_html + x.to_html() ,self.children)
        return f"<{self.tag}></{self.tag}>"