class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums2)
        s, nxt = [], {}
        for i, n in enumerate(nums2):
            while s and s[-1] < n:
                l = s.pop()
                if l not in nxt:
                    nxt[l] = n
            s.append(n)    
        return [nxt[n] if n in nxt else -1 for n in nums1]    