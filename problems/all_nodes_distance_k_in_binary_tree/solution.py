# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root is None:
            return
        if K == 0:
            return [target.val]
        output = []
        
        def K_far(node: TreeNode, i: int) -> None:
            if not node:
                return
            if i == K:
                output.append(node.val)
                return
            K_far(node.left, i + 1)
            K_far(node.right, i + 1)
        
        def helper(node: TreeNode) -> int:
            if node is None:
                return -1
            if node is target:
                K_far(node, 0)
                return 1
            L = helper(node.left)
            if L != -1:
                if L == K: 
                    output.append(node.val)
                K_far(node.right, L + 1)    
                return L + 1
            R = helper(node.right)
            if R != -1:
                if R == K: 
                    output.append(node.val)
                K_far(node.left, R + 1)
                return R + 1
            return -1    
        
        helper(root)    
        return output