from heapq import *

class Node:
    def __init__(self, id_: int, score: int):
        self.id_ = id_
        self.score = score
        
    def __str__(self):
        return '{}:{}'.format(self.id_, self.score)
        
    def __lt__(self, other):
        return self.score < other.score

class Leaderboard:
    def __init__(self):
        self.players = {}
        self.hp = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.players:
            n = Node(playerId, score)
            self.players[playerId] = n
            heappush(self.hp, n)
        else:
            self.players[playerId].score += score
            heapify(self.hp)

    def top(self, K: int) -> int:
        return sum([n.score for n in nlargest(K, self.hp)])

    def reset(self, playerId: int) -> None:
        self.players[playerId].score = 0
        heapify(self.hp)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)