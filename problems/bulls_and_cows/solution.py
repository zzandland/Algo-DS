from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        sl, gl = [], []
        for a, b in zip(secret, guess):
            if a == b: bulls += 1
            else:
                sl.append(a)
                gl.append(b)
        nums = Counter(sl)
        for c in gl:
            if c in nums:
                nums[c] -= 1
                cows += 1
                if nums[c] == 0: del nums[c]
        return '%dA%dB' % (bulls, cows)