from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = Counter(secret)
        a = b = 0
        missed = []
        for s, g in zip(secret, guess):
            if s == g:
                if freq[g] > 0:
                    a += 1
                    freq[g] -= 1
            else:
                missed.append(g)
                    
        for g in missed:
            if freq[g] > 0:
                b += 1
                freq[g] -= 1
                
        return '%dA%dB' % (a, b)