class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        res = 0
        y = x = i = 0
        dp = {}
        while y < rows:
            j = i
            if j not in dp:
                cnt = 0
                rem = cols - x
                while rem >= len(sentence[i]):
                    x += len(sentence[i]) + 1
                    i += 1
                    if i == len(sentence):
                        cnt += 1
                        i = 0
                    rem = cols - x
                x = 0
                dp[j] = (cnt, i)
            cnt, i = dp[j]
            y += 1
            res += cnt
        return res