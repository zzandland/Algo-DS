from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2, res = Counter(nums1), Counter(nums2), []
        for num in c1:
            if num in c2:
                for i in range(min(c1[num], c2[num])):
                    res.append(num)
        return res            