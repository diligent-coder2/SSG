import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "First block.\n\nSecond block.\n\nThird block."
        expected = ["First block.", "Second block.", "Third block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_blocks(self):
        markdown = "Block one.\n\n\n\nBlock two."
        expected = ["Block one.", "Block two."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_leading_and_trailing_whitespace(self):
        markdown = "\n\n  Block with leading and trailing whitespace.  \n\n"
        expected = ["Block with leading and trailing whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    class TestBlockToBlockType(unittest.TestCase):
        def test_heading(self):
            self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

        def test_quote(self):
            self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)

        def test_unordered_list(self):
            self.assertEqual(block_to_block_type("- List item"), BlockType.ULIST)

        def test_ordered_list(self):
            self.assertEqual(block_to_block_type("1. List item"), BlockType.OLIST)

        def test_code(self):
            self.assertEqual(block_to_block_type("```Code block```"), BlockType.CODE)

        def test_paragraph(self):
            self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

        def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
            block = "> quote\n> more quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
            block = "- list\n- items"
            self.assertEqual(block_to_block_type(block), BlockType.ULIST)
            block = "1. list\n2. items"
            self.assertEqual(block_to_block_type(block), BlockType.OLIST)
            block = "paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == '__main__':
    unittest.main()
