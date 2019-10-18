from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children: List[TreeNode] = []
        self.visited = False

    def add(self, child) -> None:
        self.children.append(child)
        child.parent = self


def sum_leaf_n_tree(root: TreeNode) -> int:
    output = 0

    if root is None:
        return output

    while root is not None:
        if not root.visited:
            if not root.children:
                output += root.val
            root.visited = True

        if not root.children:
            root = root.parent
        else:
            tmp = root.children[-1]
            root.children.pop()
            root = tmp

    return output


def test():
    root = TreeNode(5)
    child1 = TreeNode(3)
    child2 = TreeNode(7)
    child3 = TreeNode(9)
    root.add(child1)
    root.add(child2)
    child2.add(child3)

    return sum_leaf_n_tree(root)


print(test())
