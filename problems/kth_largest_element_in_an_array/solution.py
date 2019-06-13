class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not (0 < k <= len(nums)):
            return -1
        for i in range(len(nums) // 2, 0, -1):
            self.heapify(nums, i)
        while k > 0:
            self.heapify(nums, 0)    
            nums[0], nums[-1] = nums[-1], nums[0]
            output = nums.pop()
            k -= 1
        return output    
    
    def heapify(self, nums: List[int], i: int) -> None:
        mx = i
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < len(nums) and nums[mx] < nums[left_i]:
            mx = left_i
        if right_i < len(nums) and nums[mx] < nums[right_i]:
            mx = right_i
        if mx != i:
            nums[mx], nums[i] = nums[i], nums[mx]   
            self.heapify(nums, mx)