class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(list(tiles)))
        N, res = len(tiles), 0
        def bt(tmp: List[str]) -> int:
            nonlocal res
            if not tmp: return 0
            res = 0
            for i, t in enumerate(tmp):
                if i > 0 and t == tmp[i-1]: continue
                res += bt(tmp[:i] + tmp[i+1:]) + 1
            return res    
        return bt(tiles)