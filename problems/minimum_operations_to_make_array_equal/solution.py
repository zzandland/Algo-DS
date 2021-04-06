class Solution:
    def minOperations(self, n: int) -> int:
        '''
        1 3 5 7 9
        4 + 2
        '''
        if n == 1: return 0
        arr = []
        for i in range(n // 2):
            arr.append(i * 2 + 1)
        target = arr[-1] + 1 if n % 2 == 0 else arr[-1] + 2
        res = 0
        for n in arr: 
            res += target - n
        return res