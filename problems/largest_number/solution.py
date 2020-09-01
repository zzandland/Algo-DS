class Comp(str):
    def __lt__(a: str, b: str):
        return a + b > b + a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str, nums), key=Comp))
        return '0' if res[0] == '0' else res