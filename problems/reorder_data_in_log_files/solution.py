class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log: str):
            identifier, rest = log.split(' ', 1)
            if rest[0].isdigit(): return (1,)
            else: return (0, rest, identifier)
            
        return sorted(logs, key=key)