class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        I, J, i, j, c, prev, res = len(nums1), len(nums2), 0, 0, 0, None, []
        t = ((I+J) // 2, ) if (I+J) % 2 == 1 else ((I+J)//2-1, (I+J)//2)
        while i < I and j < J:
            if nums1[i] < nums2[j]: 
                if c in t: res.append(nums1[i])
                i, c = i+1, c+1
            elif nums1[i] > nums2[j]: 
                if c in t: res.append(nums2[j])
                j, c = j+1, c+1
            else:
                if (i < I-1 and j < J-1 and nums1[i+1] < nums2[j+1]) or i == I-1:
                    if c in t: res.append(nums1[i])
                    i, c = i+1, c+1
                else: 
                    if c in t: res.append(nums2[j])
                    j, c = j+1, c+1
        while i < I:
            if c in t: res.append(nums1[i])
            i, c = i+1, c+1    
        while j < J:
            if c in t: res.append(nums2[j])
            j, c = j+1, c+1
        return sum(res) / len(res)