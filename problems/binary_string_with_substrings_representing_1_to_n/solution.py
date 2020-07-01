class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N, 0, -1):
            t = '{0:b}'.format(i)
            bitmap = 0
            for j in range(len(S)):
                if bitmap == i: break
                bitmap <<= 1
                bitmap ^= int(S[j])
                if j >= len(t): bitmap &= ~(1 << len(t))
            else:
                if bitmap == i: continue
                return False
        return True