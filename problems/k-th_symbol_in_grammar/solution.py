class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def fn(l: int, r: int, n: int) -> int:
            if l == r: return n
            m = l + (r-l)//2
            if K <= m:
                return fn(l, m, 0 if n == 0 else 1)
            return fn(m+1, r, 1 if n == 0 else 0)
        return fn(1, 2**(N-1), 0)