class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = board[0] + board[1]
        seen = set(tuple(start))
        moves = {0: [1, 3], 1: [0, 4, 2], 2: [1, 5], 3: [0, 4], 4: [3, 1, 5], 5: [2, 4]}
        q, res = [start], 0
        while q:
            nq = []
            for b in q:
                if b == [1, 2, 3, 4, 5, 0]: return res
                zero = b.index(0)
                for m in moves[zero]:
                    tmp = b[:]
                    tmp[zero], tmp[m] = tmp[m], tmp[zero]
                    t = tuple(tmp)
                    if t not in seen:
                        seen.add(t)
                        nq.append(tmp)
            q = nq
            res += 1
        return -1