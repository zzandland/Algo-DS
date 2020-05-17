class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt, tmp, res, S = 0, [], [], len(s)
        for c in s:
            if c == ')':
                if cnt > 0:
                    tmp.append(c)
                    cnt -= 1
            else:
                if c == '(': cnt += 1
                tmp.append(c)
        cnt = 0        
        for c in tmp[::-1]:        
            if c == '(':
                if cnt > 0:
                    res.append(c)
                    cnt -= 1
            else:
                if c == ')': cnt += 1
                res.append(c)
        return ''.join(res[::-1])