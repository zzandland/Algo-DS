from typing import Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        S = len(start)
        if S != len(end): return False
        def fn(s: str) -> List[List[int]]:
            res = []
            for i, c in enumerate(s):
                if c != 'X': res.append([c, i])
            return res
        a, b = fn(start), fn(end)
        if len(a) != len(b):return False
        for i in range(len(a)):
            ac, ai = a[i]
            bc, bi = b[i]
            if ac != bc: return False
            if ac == 'L' and ai < bi: return False
            if ac == 'R' and ai > bi: return False
        return True