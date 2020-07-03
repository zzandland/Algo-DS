from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen, res = Counter(), 0
        for i, j in dominoes:
            if (i, j) in seen:
                res += seen[i, j]
            elif (j, i) in seen:
                res += seen[j, i]
            seen[i, j] += 1
            if i != j: seen[j, i] += 1
        return res