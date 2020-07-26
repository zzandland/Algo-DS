class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            digits = list(str(num))
            num = sum(map(int, digits))
        return num