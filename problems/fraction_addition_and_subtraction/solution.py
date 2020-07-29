from collections import deque

class Solution:
    def fractionAddition(self, expression: str) -> str:
        q = deque(expression)
        numr, denumr = 0, 1
        while q:
            val = q.popleft()
            while q[0] != '/':
                val += q.popleft()
            num = int(val)
            q.popleft()
            val = q.popleft()
            while q and q[0].isdigit():
                val += q.popleft()
            denum = int(val)
            if denumr % denum == 0:
                num *= denumr // denum
            else:
                newDenum = denumr * denum
                numr *= newDenum // denumr
                num *= newDenum // denum
                denumr = newDenum
            numr += num
        if numr == 0: return '0/1'
        gcd = self.gcd(abs(numr), abs(denumr))
        return '%d/%d' % (numr // gcd, denumr // gcd)
    
    def gcd(self, a: int, b: int) -> int:    
        if a == 0: return b
        if b == 0: return a
        if a == b: return a
        if a > b: return self.gcd(a-b, b)
        return self.gcd(a, b-a)