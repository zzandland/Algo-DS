class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dl, ll = [], []
        def comparator(log: str):
            f, r = log.split(' ', 1)
            if r[0].isnumeric(): return (1,)
            return (0, r, f)
        return sorted(logs, key=comparator)