class Node(object):
    def __init__(self, attrs=None):
        self.attrs = attrs or {}

    def matches(self, node):
        return False

    def is_self_closing(self, node):
        return False

    def tag(self, node, parent=None):
        return None

    def text(self, node):
        return None


