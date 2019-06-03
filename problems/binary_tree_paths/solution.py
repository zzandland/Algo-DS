# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        output, runner = [], []
        self.recurse(root, output, runner)
        return output
    
    def recurse(self, root: TreeNode, output: List[str], runner: List[int]):
        if root is None:
            return
        runner.append(str(root.val))
        if root.left is not None:
            self.recurse(root.left, output, runner)
        if root.right is not None:
            self.recurse(root.right, output, runner)
        if root.left is None and root.right is None:
            output.append('->'.join(runner))
        runner.pop()
