class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        it, seen, = cells[:], {}
        while N > 0:
            t = tuple(it)
            if t in seen: N %= seen[t]-N
            seen[tuple(it)] = N
            if N == 0: return it
            it = [int(i > 0 and i < len(cells)-1 and it[i-1] == it[i+1]) for i, _ in enumerate(it)]
            N -= 1
        return it