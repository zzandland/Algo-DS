class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirs = input.split('\n')
        res, st = 0, []
        for d in dirs:
            cnt = d.count('\t')
            name = d[cnt:]
            while st and st[-1][1] >= cnt:
                st.pop()
            if name.count('.') > 0:
                res = max(res, sum([len(x[0]) for x in st]) + len(st) + len(name))
            else:
                st.append([name, cnt])
        return res        