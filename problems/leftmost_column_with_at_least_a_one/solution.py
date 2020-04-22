# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        N, M = binaryMatrix.dimensions()
        r, c, left = 0, M-1, M
        while r < N and c >= 0:
            if binaryMatrix.get(r, c) == 0: r += 1
            else:
                left = min(left, c)    
                c -= 1
        return -1 if left == M else left