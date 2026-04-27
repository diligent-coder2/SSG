from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception(f"that's invalid Markdown syntax for {node}")
        split_text = node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if text == '':
                continue
            if i % 2 == 1:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes