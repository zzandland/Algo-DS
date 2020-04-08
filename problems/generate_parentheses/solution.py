class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fn(lst: List[str], diff: int) -> List[str]:
            if len(lst) > n*2 or diff < 0: return []
            if len(lst) == n*2 and diff == 0: return [''.join(lst)]
            return fn(lst+['('], diff+1) + fn(lst+[')'], diff-1)
        return fn([], 0)