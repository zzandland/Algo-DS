class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([n for n, nn in zip(heights, sorted(heights)) if n != nn])