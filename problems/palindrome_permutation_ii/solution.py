from collections import Counter, deque

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        c = Counter(s)
        odds = list(
            map(lambda x: x[0], 
                filter(lambda x: x[1] & 1 == 1, c.items())
            )
        )
        if len(odds) > 1: return []
        res, run = [], deque()
        def dfs() -> None:
            if not c:
                res.append(''.join(run))
                return
            for let in list(c.keys()):
                c[let] -= 2
                if c[let] == 0: del c[let]
                run.append(let)
                run.appendleft(let)
                dfs()
                c[let] += 2
                run.pop()
                run.popleft()
        if odds: 
            run.append(odds[0])
            c[odds[0]] -= 1
            if c[odds[0]] == 0: del c[odds[0]]
        dfs()
        return res