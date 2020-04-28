class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1: return math.isclose(nums[0], 24)
        for i in range(N):
            for j in range(N):
                if i != j:
                    rest = nums[:i]+nums[i+1:j]+nums[j+1:] if i < j else nums[:j]+nums[j+1:i]+nums[i+1:]
                    for ops in [self.add, self.sub, self.mul, self.div]:
                        if ops == add or ops == mul:
                            if i < j and self.judgePoint24([ops(nums[i], nums[j])] + rest): return True
                        if self.judgePoint24([ops(nums[i], nums[j])] + rest): return True
        return False        
    
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def sub(self, a: int, b: int) -> int:
        return a - b
    
    def mul(self, a: int, b: int) -> int:
        return a * b
    
    def div(self, a: int, b: int) -> int:
        return a / b if b > 0 else 0