class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def fn(x: str):
            a, rest = x.split(' ', 1)
            if rest.split()[0].isdigit(): return (1,)
            return (0, rest, a)
        return sorted(logs, key=fn)