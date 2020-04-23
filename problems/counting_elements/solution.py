from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = Counter(arr)
        return sum([freq if num+1 in c else 0 for num, freq in c.items()])