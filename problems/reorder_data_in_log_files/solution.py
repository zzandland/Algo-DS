class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comp(s: str):
            id, rest = s.split(' ', 1)
            if rest[0].isdigit(): return (1, )
            return (0, rest, id)
        logs.sort(key=comp)
        return logs