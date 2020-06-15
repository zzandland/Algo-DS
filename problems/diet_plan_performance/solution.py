class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int,
                            lower: int, upper: int) -> int:
        N = len(calories)
        run, res = sum(calories[:k]), 0
        for i in range(k, N):
            if run > upper:
                res += 1
            elif run < lower:
                res -= 1
            run += calories[i] - calories[i-k]
        if run > upper:
            res += 1
        elif run < lower:
            res -= 1
        return res