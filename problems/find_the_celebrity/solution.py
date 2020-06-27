# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i): candidate = i
        for j in range(n):
            if j == candidate: continue
            if knows(candidate, j) or not knows(j, candidate): return -1
        return candidate