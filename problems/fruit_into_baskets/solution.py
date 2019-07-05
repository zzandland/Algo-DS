class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        cnt, dic, s, e = 0, collections.defaultdict(int), 0, 0
        max_len = 0
        while e < len(tree):
            if dic[tree[e]] == 0:
                cnt += 1
            dic[tree[e]] += 1                
            e += 1
            while cnt > 2:
                dic[tree[s]] -= 1
                if dic[tree[s]] == 0:
                    cnt -= 1
                s += 1
            max_len = max(max_len, e - s)
        return max_len        