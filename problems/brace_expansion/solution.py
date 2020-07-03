class Solution:
    def expand(self, S: str) -> List[str]:
        arr = list(map(lambda x: x.split(','), filter(lambda x: x, re.compile('[{}]').split(S))))
        def dfs(i: int) -> List[int]:
            if i == len(arr): return ['']
            return [c + nc for c in arr[i] for nc in dfs(i+1)]
        return sorted(dfs(0))