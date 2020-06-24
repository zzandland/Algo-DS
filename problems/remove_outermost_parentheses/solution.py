class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        prims, cnt, tmp = [], 0, []
        for c in S:
            tmp.append(c)
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                prims.append(''.join(tmp[:])[1:-1])
                tmp = []
        return ''.join(prims)