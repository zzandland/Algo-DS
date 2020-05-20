class NumArray:
    def _update(self, l: int, r: int, i: int, t: int, val: int) -> int:
        if l == r:
            self.dp[i] = val
            return self.dp[i]
        m = l + (r-l)//2
        if t <= m: ln, rn = self._update(l, m, 2*i+1, t, val), self.dp[2*i+2]
        else: ln, rn = self.dp[2*i+1], self._update(m+1, r, 2*i+2, t, val)
        self.dp[i] = ln + rn
        return self.dp[i]
    
    def __init__(self, nums: List[int]):
        if not nums: return
        self.N = len(nums)
        x = (int)(ceil(log2(self.N)))
        self.dp = [None] * (2 * 2**x - 1)
        def fn(l: int, r: int, i: int) -> int:
            print(l, r, i)
            if l == r:
                self.dp[i] = nums[l]
            else:
                m = l + (r-l)//2
                self.dp[i] = fn(l, m, 2*i+1) + fn(m+1, r, 2*i+2)
            return self.dp[i]
        fn(0, self.N-1, 0)

    def update(self, i: int, val: int) -> None:
        self._update(0, self.N-1, 0, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def fn(d: int, l: int, r: int) -> int:
            nonlocal i, j
            if l >= i and r <= j: return self.dp[d]
            if l > j or r < i: return 0
            m = l + (r-l)//2
            return fn(2*d+1, l, m) + fn(2*d+2, m+1, r)
        return fn(0, 0, self.N-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)