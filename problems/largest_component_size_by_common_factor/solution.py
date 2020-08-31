class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        N = max(A)
        parents = list(range(N+1))
        size = [1]*(N+1)
        
        sq = int(sqrt(N)) + 1
        sieve = [True]*(sq+1)
        primes = []
        for n in range(2, sq+1):
            if sieve[n]:
                primes.append(n)
                i = 1
                while n*i <= sq:
                    sieve[n*i] = False
                    i += 1
        
        def find(u: int) -> int:
            if parents[u] != u: parents[u] = find(parents[u])
            return parents[u]
        
        def union(u: int, v: int) -> None:
            uf, vf = find(u), find(v)
            if uf == vf: return False
            if size[uf] > size[vf]: uf, vf = vf, uf
            parents[uf] = vf
            size[vf] += size[uf]
            return True
        
        for n in A:
            sq = int(sqrt(n)) + 1
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    union(n, f)
                    union(n, n // f)
                        
        cnt = Counter()
        res = 0
        
        for n in A:
            cnt[find(n)] += 1
            res = max(res, cnt[find(n)])
        return res