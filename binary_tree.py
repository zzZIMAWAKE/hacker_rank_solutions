class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if not self.find(value):
                self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)

tree = BinaryTree(6)
tree.add(3)
tree.add(16)
tree.add(1)
tree.add(0)
tree.add(35)
tree.print_tree()
