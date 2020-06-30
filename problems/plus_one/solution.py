class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lft, idx = 0, len(digits)-1
        digits[idx] += 1
        while idx > 0 and digits[idx] == 10:
            digits[idx] = 0
            idx -= 1
            digits[idx] += 1
        if digits[0] == 10: return [1, 0] + digits[1:]
        return digits