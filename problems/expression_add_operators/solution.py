import re

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        def fn(i: int, run: List[int], buf: str) -> List[str]:
            if i == N: 
                return [buf[1:]] if sum(run) == target else []
            res = []
            for j in range(i+1, N+1):
                n = num[i:j]
                if len(n) == len(str(int(n))):
                    res += fn(j, run+[int(n)], '{}+{}'.format(buf, n))
                    if i > 0:
                        res += fn(j, run+[-int(n)], '{}-{}'.format(buf, n))
                        res += fn(j, run[:-1]+[run[-1]*int(n)], '{}*{}'.format(buf, n))
            return res    
        return fn(0, [], '')