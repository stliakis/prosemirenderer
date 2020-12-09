# -*- coding: utf-8 -*-

from prosemirenderer.marks import Mark
from prosemirenderer.nodes import Node
from prosemirenderer.prosemirror import ProseMirrorRenderer
from prosemirenderer.tags import RawTag


class ProseMirror2Plain(ProseMirrorRenderer):
    def __init__(self):
        super(ProseMirror2Plain, self).__init__(
            marks=[
                Bold(),
                Code(),
                Italic(),
                Link()
            ],
            nodes=[
                Paragraph(),
                OrderedList(),
                ListItem(),
                Image(),
                Heading(),
                CodeBlock(),
                BulletList(),
                BlockQuote()
            ]
        )


class Bold(Mark):
    def matches(self, mark):
        return mark.get("type") == "bold"

    def tag(self, mark, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class Code(Mark):
    def matches(self, mark):
        return mark.get("type") == "code"

    def tag(self, mark, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class Italic(Mark):
    def matches(self, mark):
        return mark.get("type") == "italic"

    def tag(self, mark, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class Link(Mark):
    def matches(self, mark):
        return mark.get("type") == "link"

    def tag(self, mark, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class BlockQuote(Node):
    def matches(self, node):
        return node.get("type") == "blockquote"

    def tag(self, node, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class BulletList(Node):
    def matches(self, node):
        return node.get("type") == "bullet_list"

    def tag(self, node, parent=None):
        return RawTag(opening_tag=None, closing_tag="\n")


class CodeBlock(Node):
    def matches(self, node):
        return node.get("type") == "code_block"

    def tag(self, node, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class Heading(Node):
    def matches(self, node):
        return node.get("type") == "heading"

    def tag(self, node, parent=None):
        return RawTag(opening_tag="\n", closing_tag="\n")


class Image(Node):
    def matches(self, node):
        return node.get("type") == "image"

    def is_self_closing(self, node):
        return True

    def tag(self, node, parent=None):
        return RawTag(opening_tag=None, closing_tag=None)


class ListItem(Node):
    def matches(self, node):
        return node.get("type") == "list_item"

    def tag(self, node, parent=None):
        return RawTag(opening_tag=u'  • ', closing_tag=None)


class OrderedList(Node):
    def matches(self, node):
        return node.get("type") == "ordered_list"

    def tag(self, node, parent=None):
        return RawTag(opening_tag=u'  • ', closing_tag="\n")


class Paragraph(Node):
    def matches(self, node):
        return node.get("type") == "paragraph"

    def tag(self, node, parent=None):
        if not parent or parent.get("type") != "list_item":
            return RawTag(opening_tag=None, closing_tag="\n\n")
        else:
            return RawTag(opening_tag=None, closing_tag="\n")
