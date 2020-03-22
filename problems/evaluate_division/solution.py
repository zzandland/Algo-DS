from collections import defaultdict
from fractions import Fraction as frac

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(dict)
        for [frm, to], val in zip(equations, values):
            dic[frm][to] = frac(str(val))
            dic[to][frm] = frac(str(1 / val))
            
        visited = set()
        def traverse(to: str, n: str) -> int:
            if to == n:
                return 1
            for nxt, val in dic[n].items():
                if nxt not in visited:
                    visited.add(nxt)
                    cal = traverse(to, nxt)
                    if cal != -1:
                        return val * cal
            return -1
            
        output = []    
        for [frm, to] in queries:
            if frm not in dic or to not in dic:
                output.append(float(-1))
            else:    
                visited.add(frm)
                cal = traverse(to, frm)
                if cal == -1.0:
                    output.append(float(-1))
                else:    
                    output.append(cal)
                    dic[frm][to] = frac(str(cal))
                    dic[to][frm] = frac(str(1 / cal))
                visited.clear()
        return output        