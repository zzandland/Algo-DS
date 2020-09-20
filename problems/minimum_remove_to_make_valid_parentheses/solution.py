class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)
        tmp = [True]*N
        def helper(front: bool):
            ran = range(N) if front else range(N-1, -1, -1)
            cnt = 0
            for i in ran:
                c = s[i]
                if front:
                    if c == '(': cnt += 1
                    elif c == ')':
                        if cnt == 0: tmp[i] = False
                        else: cnt -= 1
                else:
                    if c == ')': cnt += 1
                    elif c == '(':
                        if cnt == 0: tmp[i] = False
                        else: cnt -= 1
        helper(True)
        helper(False)
        res = []
        for i in range(N):
            if tmp[i]: res.append(s[i])
        return ''.join(res)