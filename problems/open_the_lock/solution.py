class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ds = {*deadends}
        if '0000' in ds: return -1
        ds.add('0000')
        q = {'0000'}
        res = 0
        while q:
            nq = set()
            if target in q: return res
            res += 1
            for s in q:
                for i in range(4):
                    l = s[:i] + str((int(s[i]) + 9) % 10) + s[i+1:]
                    if l not in ds:
                        ds.add(l)
                        nq.add(l)
                    r = s[:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
                    if r not in ds:
                        ds.add(r)
                        nq.add(r)
            q = nq
        return -1