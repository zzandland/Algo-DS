class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l = False, 0
        for c in s:
            if c == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
                if c == 'A':
                    if a:
                        return False
                    else:
                        a = True
        return True        