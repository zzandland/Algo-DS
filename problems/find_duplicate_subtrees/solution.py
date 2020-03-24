# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans = []
        count = defaultdict(int)
        def collect(n: TreeNode) -> str:
            if not n: return '#'
            serial = '{}, {}, {}'.format(n.val, collect(n.left), collect(n.right))
            count[serial] += 1
            if count[serial] == 2: ans.append(n)
            return serial    
        collect(root)        
        return ans