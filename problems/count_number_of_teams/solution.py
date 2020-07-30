class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        # asc cases
        asc = [1]*N
        desc = [1]*N
        for k in range(1, 3):
            for i in range(N-1, -1, -1):
                up = down = 0
                for j in range(i-1, -1, -1):
                    if rating[j] < rating[i]: up += asc[j]
                    if rating[j] > rating[i]: down += desc[j]
                asc[i], desc[i] = up, down
        return sum(asc) + sum(desc)