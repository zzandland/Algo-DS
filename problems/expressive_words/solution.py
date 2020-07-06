class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def gen(s: str):
            res = []
            let, cnt = S[0], 1
            for i in range(1, len(s)):
                c = s[i]
                if c != let:
                    res.append((let, cnt))
                    let, cnt = c, 1
                else:
                    cnt += 1
            res.append((let, cnt))
            return res
        target = gen(S)
        res = 0
        for w in words:
            wd = gen(w)
            if len(wd) == len(target):
                for a, b in zip(target, wd):
                    tc, tf = a
                    wc, wf = b
                    if tc != wc or tf < wf: break
                    if tf == 2 and tf > wf: break
                else:
                    res += 1
        return res