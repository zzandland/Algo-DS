class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        def find(n: int) -> int:
            UF.setdefault(n, n)
            if UF[n] != n: UF[n] = find(UF[n])
            return UF[n]
        def union(a: int, b: int) -> None:
            UF[find(a)] = find(b)
        for y, x in stones:
            union(y, x + 10000)    
        return len(stones) - len({find(x) for x in UF})   