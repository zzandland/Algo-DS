class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log: str) -> int:
            id_, r = log.split(' ', 1)
            if r[0].isdigit(): return (1, )
            return (0, r, id_)
        return sorted(logs, key=key)