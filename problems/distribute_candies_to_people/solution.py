class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        cur, prev, cnt = 0, -1, 1
        while candies >= 0:
            res[cur] += cnt
            candies -= cnt
            cur, prev = (cur+1) % num_people, cur
            cnt += 1
        res[prev] += candies
        return res