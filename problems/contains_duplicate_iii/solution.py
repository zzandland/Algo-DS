class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val: int, root: Node) -> Node:
        if not root: return Node(val)
        if root.val > val: root.left = self.insert(val, root.left)
        else: root.right = self.insert(val, root.right)
        return root
    
    def query(self, val: int, k: int) -> bool:
        n = self.root
        while n:
            if abs(val - n.val) <= k: return True
            if n.val > val: n = n.left
            else: n = n.right
        return False
    
    def delete(self, val: int, root: Node) -> Node:
        if not root: return None
        if root.val == val:
            if root.left and root.right:
                tmp = root.right
                while tmp.left: tmp = tmp.left
                root.val = tmp.val
                root.right = self.delete(tmp.val, root.right)
            elif not root.left: return root.right
            else: return root.left
        else:
            if root.val > val: root.left = self.delete(val, root.left)
            else: root.right = self.delete(val, root.right)
        return root

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bst = BST()
        for i, n in enumerate(nums):
            if i-k > 0: bst.root = bst.delete(nums[i-k-1], bst.root)
            if bst.query(n, t): return True
            bst.root = bst.insert(n, bst.root)
        return False