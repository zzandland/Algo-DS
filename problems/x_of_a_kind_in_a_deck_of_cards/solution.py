from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def getPrimes(n: int) -> [int]: 
            sieve = [True] * (n + 1)
            res = []
            for i in range(2, n+1):
                if sieve[i]:
                    j = 1
                    res.append(i)
                    while i*j < n+1:
                        sieve[i*j] = False
                        j += 1
            return res
        
        c = Counter(deck)
        vals = c.values()
        primes = getPrimes(min(vals))
        for p in primes:
            for v in c.values():
                if v % p != 0: break
            else: return True
        return False