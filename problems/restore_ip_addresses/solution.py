class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        def dfs(i: int, tmp: List[str]) -> None:
            nonlocal res
            if len(tmp) > 4: return
            if i >= len(s):
                if len(tmp) == 4: res.add('.'.join(tmp))
                return
            for j in range(1, 4):
                if j > 1 and s[i] == '0': break
                if int(s[i:i+j]) <= 255:
                    tmp.append(s[i:i+j])
                    dfs(i+j, tmp)
                    tmp.pop()
        dfs(0, [])
        return res