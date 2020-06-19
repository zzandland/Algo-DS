class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        prefix, dic, run = [float('inf')]*N, {0: 0}, 0
        for i in range(1, N):
            run += arr[i-1]
            tmp = float('inf')
            if run-target in dic:
                tmp = i - dic[run-target]
            prefix[i] = min(prefix[i-1], tmp)
            dic[run] = i
        suffix, dic, run = [float('inf')]*N, {0: N}, 0
        for j in range(N-1, -1, -1):
            run += arr[j]
            tmp = float('inf')
            if run-target in dic:
                tmp = dic[run-target] - j
            suffix[j] = min(suffix[j-1], tmp)
            dic[run] = j
        res = min([a + b for a, b in zip(prefix, suffix)])
        return res if res != float('inf') else -1