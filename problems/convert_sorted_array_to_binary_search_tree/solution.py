# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      def helper(left: int, right: int) -> TreeNode:
        if left > right:
          return None
        mid = left + (right - left) // 2
        n = TreeNode(nums[mid])
        n.left = helper(left, mid - 1)
        n.right = helper(mid + 1, right)
        return n
      return helper(0, len(nums) - 1)