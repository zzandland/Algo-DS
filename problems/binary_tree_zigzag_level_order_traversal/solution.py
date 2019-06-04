# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if root is None:
            return output
        q = collections.deque()
        q.append(root)
        reverse = False
        while len(q) > 0:
            k = len(q)
            level = []
            for i in range(k):
                node = q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:    
                    q.append(node.right)
            if reverse is True:
                level.reverse()
            output.append(level)
            reverse = not reverse    
        return output        