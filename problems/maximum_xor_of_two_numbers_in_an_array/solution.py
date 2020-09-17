class Trie:
    def __init__(self):
        self.one = self.zero = self.val = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        for n in nums:
            cur = root
            for i in range(31, -1, -1):
                masked = n & (1 << i)
                if masked == 0:
                    if not cur.zero: cur.zero = Trie()
                    cur = cur.zero
                else:
                    if not cur.one: cur.one = Trie()
                    cur = cur.one
            cur.val = n
            
        res = 0
        for n in nums:
            cur = root
            for i in range(31, -1, -1):
                masked = n & (1 << i)
                if masked == 0:
                    if cur.one: cur = cur.one
                    else: cur = cur.zero
                else:
                    if cur.zero: cur = cur.zero
                    else: cur = cur.one
            res = max(res, n ^ cur.val)
        return res