class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        V = list(range(n))
        
        def find(i: int) -> int:
            if i != V[i]:
                V[i] = find(V[i])
            return V[i]
        
        def union(a: int, b: int) -> None:
            V[find(a)] = find(b)
            
        for u, v in edges:
            union(u, v)
        return len([i for i in range(n) if V[i] == i])