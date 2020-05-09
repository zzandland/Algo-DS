class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        ids, d = set(), {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                ids.add(i)
            elif c in d:
                j = d[c]
                if j in ids: ids.remove(j)
        return min(ids) if ids else -1