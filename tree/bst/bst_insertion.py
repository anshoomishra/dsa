class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = self.right = None


def insert(root,data):
    if not root:
        return TreeNode(data)
    if root.left < data:
        root.right = insert(root.right,data)
    if root.right > data:
        root.left = insert(root.left,data)
    return root

