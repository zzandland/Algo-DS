class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        hp = []
        for i in range(len(indexes)):
            heapq.heappush(hp, (-1 * indexes[i], sources[i], targets[i]))
        while len(hp) > 0:
            index, source, target = heapq.heappop(hp)
            index *= -1
            if (S[index:index+len(source)]) == source:
                S = S[:index] + target + S[index + len(source):]
        return S