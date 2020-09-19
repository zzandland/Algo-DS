class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        bucket = [[] for _ in range(9)]
        for i in range(1, 10):
            tmp = 0
            for j in range(i, 10):
                tmp = tmp*10 + j
                if tmp > high: break
                if low <= tmp <= high: bucket[int(math.log10(tmp))].append(tmp)
        return reduce(lambda a, b: a + b, bucket)