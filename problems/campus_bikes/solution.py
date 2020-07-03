class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def key(wi: int, bi: int) -> tuple:
            wy, wx = workers[wi]
            by, bx = bikes[bi]
            return (abs(wy-by) + abs(wx-bx), wi, bi)
        comb = sorted([(i, j) for i in range(len(workers)) for j in range(len(bikes))], key=lambda x: key(*x))
        seenw, seenb = set(), set()
        res = [0]*len(workers)
        for wi, bi in comb:
            if wi not in seenw and  bi not in seenb:
                res[wi] = bi
                seenw.add(wi)
                seenb.add(bi)
        return res