from heapq import heappush, heappop

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # linearize the board
        b, reverse = [0], False
        for i in range(len(board)-1, -1, -1):
            if not reverse: b += board[i]
            else: b += board[i][::-1]
            reverse = not reverse
        
        N = len(b)
        # greedily move forward with smallest moves
        q = [(0, 1)]
        seen = {1: 0}
        while q:
            mv, pos = heappop(q)
            if pos >= N-1: return mv
            for i in range(pos+1, min(pos+7, N)):
                if i not in seen or mv < seen[i]:
                    seen[i] = mv
                    if b[i] != -1: heappush(q, (mv+1, b[i]))
                    else: heappush(q, (mv+1, i))
        return -1