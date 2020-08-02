"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        tree_root = TreeNode(root.val)
        first = tree_child = None
        for child in root.children:
            tmp = self.encode(child)
            if tree_child: tree_child.right = tmp
            tree_child = tmp
            if not first: first = tree_child
        tree_root.left = first
        return tree_root
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
        root = Node(data.val)
        children = []
        if child := data.left:
            while child:
                tmp = self.decode(child)
                children.append(tmp)
                child = child.right
        root.children = children
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))