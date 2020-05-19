from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        a, b = [], []
        for i, g in enumerate(guess):
            if g == secret[i]: A += 1
            else:
                a.append(secret[i])
                b.append(g)
        B, c = 0, Counter(a)
        for x in b:
            if c[x] > 0:
                B, c[x] = B+1, c[x]-1
        return '{}A{}B'.format(A, B)        