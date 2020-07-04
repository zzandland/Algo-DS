from collections import Counter, defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        bucket = [[] for _ in range(len(arr)+1)]
        for n, cnt in c.items():
            bucket[cnt].append(n)
        found, res = False, 0
        for i, cnts in enumerate(bucket[1:], 1):
            for _ in cnts:
                k -= i
                if k <= 0: found = True
                if k < 0 and found: res += 1
        return res