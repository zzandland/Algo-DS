class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = b = 0
        res = []
        while a < len(A) and b < len(B):
            au, av = A[a]
            bu, bv = B[b]
            if av < bu: a += 1
            elif bv < au: b += 1
            elif av < bv:
                res.append([max(au, bu), min(av, bv)])
                a += 1
            else:
                res.append([max(au, bu), min(av, bv)])
                b += 1
        return res