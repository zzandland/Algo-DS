# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        x2y2val = {}
        while q:
            n, y, x = q.popleft()
            x2y2val.setdefault(x, defaultdict(list))
            x2y2val[x][y].append(n.val)
            if n.left: q.append((n.left, y+1, x-1))
            if n.right: q.append((n.right, y+1, x+1))
        tmp = x2y2val.keys()
        mnx, mxx = min(tmp), max(tmp)
        res = []
        for x in range(mnx, mxx+1):
            tmp = []
            for _, vals in sorted(x2y2val[x].items()):
                tmp += sorted(vals)
            res.append(tmp)
        return res