class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        total = reduce(lambda x, y: x* y, range(1, n+1))
        k -= 1
        res = []
        valid = list(range(1, n+1))
        for i in range(n, 0, -1):
            m = total // i
            total //= i
            idx, k = divmod(k, m)
            res.append(str(valid.pop(idx)))
        return ''.join(res)