from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2: return False
        c = Counter(deck)
        if len(c) == 1: return True
        mn = min(c.values())
        
        primes = []
        sieve = [True]*(mn+1)
        for i in range(2, mn+1):
            if sieve[i]:
                primes.append(i)
                j = 1
                while i*j <= mn:
                    sieve[i*j] = False
                    j += 1
        
        for p in primes:
            for n in c:
                if c[n] % p != 0: break
            else: return True
        return False