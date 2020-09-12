class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        left = {*list(string.ascii_lowercase)}
        adj = {}
        for a, b in zip(str1, str2):
            if a in adj and adj[a] != b: return False
            adj[a] = b
            if b in left: left.remove(b)
        return left