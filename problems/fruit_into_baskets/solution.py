from collections import Counter

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        st, j, res = Counter(), 0, 0
        for i, f in enumerate(tree):
            st[f] += 1
            while len(st) > 2:
                st[tree[j]] -= 1
                if st[tree[j]] == 0: del st[tree[j]]
                j += 1
            res = max(res, i-j+1)
        return res