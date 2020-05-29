from collections import deque

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B: return []
        A, B, res = deque(A), deque(B), []
        while A and B:
            a = True if A[0][1] > B[0][1] else False
            if a:
                if A[0][0] <= B[0][1]:
                    res.append([max(A[0][0], B[0][0]), min(A[0][1], B[0][1])])
                B.popleft()
            else:
                if B[0][0] <= A[0][1]:
                    res.append([max(A[0][0], B[0][0]), min(A[0][1], B[0][1])])
                A.popleft()
        return res    