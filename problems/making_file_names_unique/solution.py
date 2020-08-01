from collections import Counter

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = set()
        cnts = Counter()
        def dfs(name: str, cnt: int) -> str:
            with_b = name + '(%d)' % cnt if cnt > 0 else name
            if with_b not in seen:
                seen.add(with_b)
                cnts[name] = cnt
                return with_b
            else:
                return dfs(name, cnt+1)
        return [dfs(name, cnts[name]) for name in names]