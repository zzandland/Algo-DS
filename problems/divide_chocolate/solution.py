class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if K == 0: return sum(sweetness)
        l, r = min(sweetness), sum(sweetness) // K
        
        while l < r:
            m = l + (r-l)//2
            cnt = run = 0
            
            for n in sweetness:
                run += n
                if run >= m:
                    cnt += 1
                    run = 0
            
            if cnt > K: l = m+1
            else: r = m
        return l - 1