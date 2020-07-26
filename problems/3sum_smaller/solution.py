class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # sort so we can use two pointers O(n log n)
        nums.sort()
        res = 0
        # iterate each num O(n) -> O(n^2)
        for i, n in enumerate(nums):
            # two pointers from i+1 and end of arr O(n)
            l, r = i+1, len(nums)-1
            rest = target - n
            while l < r:
                if nums[l] + nums[r] < rest:
                    print(i, l, r)
                    res += r - l
                    l += 1
                else: r -= 1
                    
        return res