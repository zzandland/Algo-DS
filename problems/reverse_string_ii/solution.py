class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        reverse = True
        for i in range(0, len(s), k):
            substr = s[i:i+k]
            if reverse: res.append(substr[::-1])
            else: res.append(substr)
            reverse = not reverse
        return ''.join(res)