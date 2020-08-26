class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        def helper(i: int, tmp: List[str]) -> None:
            nonlocal res
            if i == len(digits):
                res.append(''.join(tmp))
                return
            for c in dic[int(digits[i])]:
                tmp.append(c)
                helper(i+1, tmp)
                tmp.pop()
        helper(0, [])       
        return res