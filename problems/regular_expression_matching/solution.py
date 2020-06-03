class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        def fn(i: int, j: int) -> bool:
            if i == S and j == P:
                return True
            if j == P:
                return False
            if i == S:
                r = p[j:]
                return len(r) % 2 == 0 and all([r[k] == '*' for k in range(1, len(r), 2)])
            a, b = s[i], p[j]
            if j+1 < P and p[j+1] == '*':
                if b == '.':
                    return any([fn(i+k, j+2) for k in range(S-i+1)])
                elif a == b:
                    run = 0
                    while run+i < S and s[run+i] == b:
                        if fn(run+i, j+2):
                            return True
                        run += 1
                    return fn(run+i, j+2)    
                else:
                    return fn(i, j+2)
            elif a == b or b == '.':
                    return fn(i+1, j+1)
            return False
        return fn(0, 0)    