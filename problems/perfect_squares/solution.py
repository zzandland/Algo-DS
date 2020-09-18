class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        sqs = []
        while i*i <= n:
            sqs.append(i*i)
            i += 1
            
        q = {n}
        res = 0
        
        while True:
            nq = set()
            res += 1
            for i in q:
                for sq in sqs:
                    if i - sq == 0: return res
                    if i - sq > 0: nq.add(i - sq)
            q = nq