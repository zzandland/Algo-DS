class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        N, lt, cnt, i, j = len(chars), chars[0], 1, 1, 1
        while i < N:
            while j < N and chars[j] == lt:
                cnt += 1
                j += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[i] = c
                    i += 1
            if j == N: return i
            chars[i] = lt = chars[j]
            cnt = 0
            i += 1
        return i