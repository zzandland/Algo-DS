class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def fn(s1: str, s2: str) -> str:
            if not s1 or not s2:
                return s1 if s1 else s2
            elif len(s2) > len(s1):
                return fn(s2, s1)
            elif s1[:len(s2)] == s2:
                return fn(s1[len(s2):], s2)
            else:
                return ''
        return fn(str1, str2)