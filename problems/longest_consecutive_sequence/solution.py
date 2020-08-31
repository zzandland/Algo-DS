class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        st = set(nums)
        
        parents = {}
        size = {}
        
        for n in nums:
            parents[n] = n
            size[n] = 1
        
        def find(u: int):
            if u not in parents: return None
            if u != parents[u]: parents[u] = find(parents[u])
            return parents[u]
        
        def union(u: int, v: int) -> None:
            uf, vf = find(u), find(v)
            if uf is None or vf is None or uf == vf: return
            if size[uf] < size[vf]: uf, vf = vf, uf
            parents[vf] = uf
            size[uf] += size[vf]
            
        for n in nums:
            union(n, n+1)
            union(n, n-1)
            
        return max(size.values() or [0])