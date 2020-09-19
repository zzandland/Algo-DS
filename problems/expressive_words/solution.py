class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def convert(s: str) -> [(str, int)]:
            if not s: return []
            cnt = 1
            c = s[0]
            res = []
            for i in range(1, len(s)):
                if s[i] == c:
                    cnt += 1
                else:
                    res.append((c, cnt))
                    c, cnt = s[i], 1
            res.append((c, cnt))
            return res
        
        t = convert(S)
        res = 0
        for w in words:
            v = convert(w)
            if len(t) == len(v):
                for a, b in zip(t, v):
                    if a[0] != b[0]: break
                    if a[1] < b[1]: break
                    if a[1] <= 2 and a[1] != b[1]: break
                else:
                    res += 1
        return res