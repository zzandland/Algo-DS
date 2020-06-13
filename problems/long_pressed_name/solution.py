class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def fn(s: str) -> List[List[int]]:
            res, ch, cnt = [], s[0], 0
            for c in s:
                if c != ch:
                    res.append([ch, cnt])
                    ch, cnt = c, 1
                else:
                    cnt += 1
            res.append([ch, cnt])
            return res
        nx, tx = fn(name), fn(typed)
        return len(nx) == len(tx) and all([n == t and nc <= tc for (n, nc), (t, tc) in zip(nx, tx)])