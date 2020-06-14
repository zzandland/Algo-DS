from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c, a, b = Counter(arr1), [], []
        for n in arr2:
            for _ in range(c[n]):
                a.append(n)
            del c[n]
        for n in c:
            for _ in range(c[n]):
                b.append(n)
        return a + sorted(b)