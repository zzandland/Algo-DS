class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        N = len(digits)
        def fn(i: int, s: str) -> List[str]:
            if i == N: return [s]
            output = []
            for c in chars[int(digits[i])]:
                output += fn(i+1, s+c)
            return output    
        return fn(0, '')