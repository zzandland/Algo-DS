class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.')[::-1], version2.split('.')[::-1]
        while v1 or v2:
            a = int(v1.pop()) if v1 else 0
            b = int(v2.pop()) if v2 else 0
            if a < b: return -1
            if a > b: return 1
        return 0