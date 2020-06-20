class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        total, rem, t, res, run = math.factorial(n), list(range(1, n+1)), k-1, '', 0
        while n > 0:
            div = total // n
            res += str(rem.pop(t // div))
            t %= div
            total //= n
            n -= 1
        return res