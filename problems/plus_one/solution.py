class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return [1]
        N, lft = len(digits), 0
        for i in range(N-1, -1, -1):
            digits[i] += lft
            if i == N-1: digits[i] += 1
            if digits[i] == 10:
                lft = 1
                digits[i] = 0
            else: lft = 0    
        if lft > 0: return [lft] + digits        
        return digits