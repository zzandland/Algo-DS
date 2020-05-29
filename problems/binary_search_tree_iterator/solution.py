# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.st.pop()
        run = n.right
        while run:
            self.st.append(run)
            run = run.left
        return n.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.st

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()