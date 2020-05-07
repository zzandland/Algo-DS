from typing import Tuple

class Solution:
    def solveEquation(self, equation: str) -> str:
        if not equation: return 'Infinite solutions'
        if '=' not in equation: return 'No solution'
        lr, rr = [0, 0], [0, 0]
        le, re = equation.split('=')
        def solve(r: Tuple[int, int], e: str) -> None:
            i = 0
            if e[i] not in ('+', '-'): e = '+' + e
            while i < len(e):
                j, b = i+1, e[i]
                while j < len(e) and e[j] not in ('+', '-'):
                    b += e[j]
                    j += 1
                if b[0] == '+':
                    if b[-1] == 'x': r[0] += int(b[1:-1]) if len(b) > 2 else 1
                    else: r[1] += int(b)    
                elif b[0] == '-':
                    if b[-1] == 'x': r[0] -= int(b[1:-1]) if len(b) > 2 else 1
                    else: r[1] += int(b)    
                i = j
        if le: solve(lr, le)
        if re: solve(rr, re)
        x, c = lr[0] - rr[0], rr[1] - lr[1]
        if x == 0 and c == 0: return 'Infinite solutions'
        if x == 0: return 'No solution'
        return 'x={}'.format(c // x)