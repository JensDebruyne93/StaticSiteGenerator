import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_difTextType(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    def test_None(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "None")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is not a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
    def test_URL(self):
        node = TextNode("This is a text node", TextType.LINK, "http/www/com")
        node2 = TextNode("This is a text node", TextType.LINK, "http/www.com")
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()