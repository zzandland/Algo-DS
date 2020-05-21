class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        cnt = [0]*N
        def mergeSort(l: int, r: int) -> None:
            if l < r:
                m = l + (r-l)//2
                mergeSort(m+1, r)
                for i in range(l, m+1):
                    f = bs(nums[i], m+1, r)
                    cnt[i] += f-m
                mergeSort(l, m)
                p1, p3, tmp, p2 = m, r, nums[m+1:r+1], r-m-1
                while p1 >= l and p2 >= 0:
                    if nums[p1] > tmp[p2]:
                        nums[p3] = nums[p1]
                        p1 -= 1
                    else:
                        nums[p3] = tmp[p2]
                        p2 -= 1
                    p3 -= 1
                while p1 >= l:
                    nums[p3] = nums[p1]
                    p1, p3 = p1-1, p3-1
                while p2 >= 0:
                    nums[p3] = tmp[p2]
                    p2, p3 = p2-1, p3-1
        
        def bs(t: int, l: int, r: int) -> int:
            while l < r:
                m = l + (r-l)//2
                if nums[m] < t and nums[m+1] >= t: return m
                if nums[m] < t: l = m+1
                else: r = m
            return l if nums[l] < t else l-1
        
        mergeSort(0, N-1)
        return cnt