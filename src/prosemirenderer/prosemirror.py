from tags import RawTag


class ProseMirrorRenderer(object):

    def __init__(self, marks=[], nodes=[], join_string=""):
        self.join_string = join_string
        self.marks = marks
        self.nodes = nodes

    def get_nodes(self):
        return self.nodes

    def get_marks(self):
        return self.marks

    def render_text(self, text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'",
                                                                                                                   "&#039;")

    def render_opening_tag(self, tags):
        if not tags:
            return None

        if not isinstance(tags, list):
            tags = [tags]

        items = []
        for tag in tags:
            if isinstance(tag, RawTag):
                items.append(tag.opening_tag)
                continue

            if isinstance(tag, basestring):
                items.append("<%s>" % (tag))
                continue

            attrs = ""
            if tag.get("attrs"):
                for attribute, value in tag.get("attrs").items():
                    if value:
                        attrs += ' %s="%s"' % (attribute, value)

            items.append("<%s%s>" % (tag.get("tag"), attrs))

        return "".join([i for i in items if i])

    def render_closing_tag(self, tags):
        if not tags:
            return None

        if not isinstance(tags, list):
            tags = [tags]

        items = []

        for tag in tags:
            if isinstance(tag, RawTag):
                items.append(tag.closing_tag)
                continue

            if isinstance(tag, basestring):
                items.append("</%s>" % (tag))
                continue

            items.append("</%s>" % tag.get("tag"))

        return "".join([i for i in items if i])

    def render(self, document):
        rendered_parts = []

        for content in document.get("content"):
            rendered_parts.append(self.render_node(content))

        return self.join_string.join(rendered_parts)

    def render_node(self, node, parent_node=None):
        rendered_nodes = []

        if node.get("marks"):
            for node_mark in node.get("marks"):
                for mark in self.get_marks():
                    if mark.matches(node_mark):
                        rendered_nodes.append(self.render_opening_tag(mark.tag(node_mark, parent=parent_node)))

        for node_renderer in self.get_nodes():
            if node_renderer.matches(node):
                rendered_nodes.append(self.render_opening_tag(node_renderer.tag(node, parent=parent_node)))
                break

        if node.get("content"):
            for nested_node in node.get("content"):
                rendered_nodes.append(self.render_node(nested_node, parent_node=node))
        elif node.get("text"):
            rendered_nodes.append(self.render_text(node.get("text")))
        elif node_renderer:
            rendered_nodes.append(node_renderer.text(node))

        for node_renderer in self.get_nodes():
            if node_renderer.is_self_closing(node):
                continue

            if node_renderer.matches(node):
                rendered_nodes.append(
                    self.render_closing_tag(node_renderer.tag(node, parent=parent_node))
                )

        if node.get("marks"):
            for node_mark in reversed(node.get("marks")):
                for mark in self.get_marks():
                    if mark.matches(node_mark):
                        rendered_nodes.append(self.render_closing_tag(mark.tag(node_mark, parent=parent_node)))

        rendered_nodes = [i for i in rendered_nodes if i]

        return self.join_string.join(rendered_nodes)
