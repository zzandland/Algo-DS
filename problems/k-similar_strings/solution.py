from typing import Generator

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        N = len(A)
        def nei(a: str) -> Generator[int, None, None]:
            i = 0
            while a[i] == B[i]: i += 1
            for j in range(i+1, N):
                if a[j] == B[i] and a[j] != B[j]:
                    yield a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                    
        q, seen = [(A, 0)], set([A])
        for x, d in q:
            if x == B: return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y)
                    q.append((y, d+1))