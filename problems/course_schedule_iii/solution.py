from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        q = []
        cur = 0
        for t, d in courses:
            heappush(q, -t)
            cur += t
            if cur > d:
                cur += heappop(q)
        return len(q)