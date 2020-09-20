class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        q = {0}
        for s in stones:
            nq = set()
            for w in q:
                nq.add(w-s)
                nq.add(w+s)
            q = nq
        return min(map(abs, q))