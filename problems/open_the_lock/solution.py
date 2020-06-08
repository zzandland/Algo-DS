from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q, dead, seen, tries = deque(['0000']), set(deadends), set(), 0
        if '0000' in dead:
            return -1
        r = [['9','1'],['0','2'],['1','3'],['2','4'],['3','5'],['4','6'],['5','7'],['6','8'],['7','9'],['8','0']]
        while q:
            l = len(q)
            tries += 1
            for _ in range(l):
                n = q.popleft()
                for nn in [n[:i]+nd+n[i+1:] for i in range(4) for nd in r[int(n[i])]]:
                    if nn == target:
                        return tries
                    if nn not in seen and nn not in dead:
                        q.append(nn)
                        seen.add(nn)
        return -1