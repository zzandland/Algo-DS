class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l, r = 0, N-1
        while l <= r:
            m = l + (r-l)//2
            c = citations[m]
            if c == N-m:
                return N-m
            if c < N-m:
                l = m+1
            else:
                r = m-1
        return N-l