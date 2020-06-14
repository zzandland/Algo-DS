from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = Counter({0: 1})
        run = res = 0
        for n in A:
            run += n
            res += dic[run % K]
            dic[run % K] += 1
        return res