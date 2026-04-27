from textnode import TextNode, TextType
import re


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

def extract_markdown_images(text):
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text)

def extract_markdown_links(text):
    return re.findall(r'\[(.*?)\]\((.*?)\)', text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        split_text = re.split(r'!\[.*?\]\(.*?\)', node.text)
        for i, text in enumerate(split_text):
            if text == '':
                continue
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
            if i < len(images):
                alt, src = images[i]
                new_nodes.append(TextNode(alt, TextType.IMAGE, url=src))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        split_text = re.split(r'\[.*?\]\(.*?\)', node.text)
        for i, text in enumerate(split_text):
            if text == '':
                continue
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
            if i < len(links):
                link_text, href = links[i]
                new_nodes.append(TextNode(link_text, TextType.LINK, url=href))
    return new_nodes
