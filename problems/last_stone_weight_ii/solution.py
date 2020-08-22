class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        q = set([0])
        for s in stones:
            nq = set()
            for n in q:
                nq.add(n+s)
                nq.add(n-s)
            q = nq
        return min([n for n in nq if n >= 0])