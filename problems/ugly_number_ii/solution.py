class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q, seen = [1], set()
        p2 = p3 = p5 = 0
        def move(p: int, mul: int) -> int:
            r = q[p]*mul
            while r in seen:
                p += 1
                r = q[p]*mul
            return p
        for i in range(n-1):
            p2, p3, p5 = move(p2, 2), move(p3, 3), move(p5, 5)
            r2, r3, r5 = q[p2]*2, q[p3]*3, q[p5]*5
            mn = min(r2, r3, r5)
            if mn == r2: p2 += 1
            elif mn == r3: p3 += 1
            elif mn == r5: p5 += 1
            q.append(mn)
            seen.add(mn)
        return q[-1]