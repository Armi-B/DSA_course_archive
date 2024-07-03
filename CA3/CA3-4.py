class TreeNode:
    def __init__(self, value, father):
        self.value = value
        self.children = []
        self.father = father

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_child(self, parent, child_value):
        child = TreeNode(child_value)
        parent.children.append(child)

