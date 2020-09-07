class Node:
    
    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None

class BST:
    
    def __init__(self):
        self.root = None
        
    def add(self, val: int) -> None:
        def dfs(n: Node, val: int) -> Node:
            if not n: return Node(val)
            if val < n.val: n.left = dfs(n.left, val)
            else: n.right = dfs(n.right, val)
            return n
        self.root = dfs(self.root, val)
        
    def remove(self, val: int) -> None:
        def dfs(n: Node, val: int) -> Node:
            if not n: return None
            if n.val == val:
                if not n.left: return n.right
                if not n.right: return n.left
                right = n.right
                while right.left:
                    right = right.left
                n.val = right.val
                n.right = dfs(n.right, right.val)
            elif val < n.val: n.left = dfs(n.left, val)
            else: n.right = dfs(n.right, val)
            return n
        self.root = dfs(self.root, val)
    
    def find(self, val: int, t: int) -> bool:
        n = self.root
        while n:
            if abs(n.val - val) <= t: return True
            if val < n.val: n = n.left
            else: n = n.right
        return False

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if k < 0: return False
        bst = BST()
        
        for i, n in enumerate(nums):
            if i > k: bst.remove(nums[i-k-1])
            if bst.find(n, t):
                return True
            bst.add(n)
        return False