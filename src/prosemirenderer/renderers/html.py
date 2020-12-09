from marks import Mark
from nodes import Node
from prosemirror import ProseMirrorRenderer


class ProseMirror2HTML(ProseMirrorRenderer):
    def __init__(self):
        super(ProseMirror2HTML, self).__init__(
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
        return "strong"


class Code(Mark):
    def matches(self, mark):
        return mark.get("type") == "code"

    def tag(self, mark, parent=None):
        return "code"


class Italic(Mark):
    def matches(self, mark):
        return mark.get("type") == "italic"

    def tag(self, mark, parent=None):
        return "em"


class Link(Mark):
    def matches(self, mark):
        return mark.get("type") == "link"

    def tag(self, mark, parent=None):
        return [
            {
                "tag": "a",
                "attrs": {
                    "href": mark.get("attrs").get("href")
                }
            }
        ]


class BlockQuote(Node):
    def matches(self, node):
        return node.get("type") == "blockquote"

    def tag(self, node, parent=None):
        return {
            "tag": "blockquote",
            "attrs": self.attrs
        }


class BulletList(Node):
    def matches(self, node):
        return node.get("type") == "bullet_list"

    def tag(self, node, parent=None):
        return {
            "tag": "ul",
            "attrs": self.attrs
        }


class CodeBlock(Node):
    def matches(self, node):
        return node.get("type") == "code_block"

    def tag(self, node, parent=None):
        return [
            {
                "tag": "pre",
                "attrs": self.attrs
            },
            {
                "tag": "code",
                "attrs": self.attrs
            }
        ]


class Heading(Node):
    def matches(self, node):
        return node.get("type") == "heading"

    def tag(self, node, parent=None):
        return "h%s" % node.get("attrs").get("level")


class Image(Node):
    def matches(self, node):
        return node.get("type") == "image"

    def is_self_closing(self, node):
        return True

    def tag(self, node, parent=None):
        attrs = dict(self.attrs)
        attrs.update({
            "src": node.get("attrs").get("src"),
            "alt": node.get("attrs").get("alt"),
            "title": node.get("attrs").get("title"),
        })

        return {
            "tag": "img",
            "attrs": attrs
        }


class ListItem(Node):
    def matches(self, node):
        return node.get("type") == "list_item"

    def tag(self, node, parent=None):
        return {
            "tag": "li",
            "attrs": self.attrs
        }


class OrderedList(Node):
    def matches(self, node):
        return node.get("type") == "ordered_list"

    def tag(self, node, parent=None):
        return {
            "tag": "ol",
            "attrs": self.atts
        }


class Paragraph(Node):
    def matches(self, node):
        return node.get("type") == "paragraph"

    def tag(self, node, parent=None):
        return {
            "tag": "p",
            "attrs": self.attrs
        }
