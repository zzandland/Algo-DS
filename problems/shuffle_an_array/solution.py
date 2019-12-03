import random

class Solution:

    def __init__(self, nums: List[int]):
      self.arr = nums.copy()
      self.originalArr = nums.copy()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.originalArr.copy()
        return self.arr
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.arr)
        return self.arr
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()