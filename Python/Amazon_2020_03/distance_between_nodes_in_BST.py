from typing import List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None

def dist_between_nodes_in_BST(nums: List[int], node1: int, node2: int) -> int:
    """
    >>> dist_between_nodes_in_BST([2, 1, 3], 1, 3)
    2
    """
    root = None
    # construct BST O(nums * height of BST)
    for num in nums:
        root = insert_BST(root, num)

    # find lowest common ancestor between the nodes O(n)
    if node1 < node2: l, r = node1, node2
    else: l, r = node2, node1
    run = root
    while run:
        if l <= run.val <= r: break
        elif l > run.val: run = run.right
        elif r < run.val: run = run.left
    return depth(run, l) + depth(run, r)

def insert_BST(root: Node, val: int) -> Node:
    if not root: return Node(val)
    if root.val > val: root.left = insert_BST(root.left, val)
    else: root.right = insert_BST(root.right, val)
    return root

def depth(root: Node, val: int) -> int:
    res = 0
    while root.val != val:
        if root.val > val: root = root.left
        else: root = root.right
        res += 1
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
