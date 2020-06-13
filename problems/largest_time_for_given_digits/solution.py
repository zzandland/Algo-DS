class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        p = [str(A[0])]
        for i in range(1, len(A)):
            c, np = str(A[i]), []
            for perm in p:
                for j in range(len(perm)+1):
                    if j > 0 and perm[j-1] == c:
                        break
                    np.append(perm[:j]+c+perm[j:])
            p = np
        def key(s: str) -> int:
            s = list(map(int, list(s)))
            if s[0] > 2 or s[2] > 5 or s[0] == 2 and s[1] > 3:
                return 0
            return s[0]*600 + s[1]*60 + s[2]*10 + s[3]
        mx = max(p, key=key)
        if not key(mx) and mx != '0000':
            return ''
        return "%s:%s" % (mx[:2], mx[2:])