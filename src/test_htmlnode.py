import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="p", value="Hello, world!", children=[], props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "text", "id": "intro"})
        self.assertEqual(node.props_to_html(), ' class="text" id="intro"')

    def test_props_to_html_empty(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", props={"class": "text"})
        parent_node = ParentNode("div", [child_node], props={"id": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="container"><span class="text">child</span></div>'
        )

if __name__ == "__main__":
    unittest.main()