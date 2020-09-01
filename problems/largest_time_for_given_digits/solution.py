class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        q = ['']
        for d in A:
            nq = []
            for n in q:
                for i in range(len(n)+1):
                    nq.append(n[:i] + str(d) + n[i:])
            q = nq
        filtered = list(filter(lambda x: int(x[:2]) < 24 and int(x[2:]) < 60, q))
        if not filtered: return ''
        mx = max(filtered, key=lambda x: int(x[:2]) * 60 + int(x[2:]))
        return mx[:2] + ':' + mx[2:]