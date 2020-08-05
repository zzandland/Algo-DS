class FileSharing:

    def __init__(self, m: int):
        self.chunks = [set() for _ in range(m+1)]
        self.ids = [1]
        self.users = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        id_ = heappop(self.ids)
        for chunk in ownedChunks:
            self.chunks[chunk].add(id_)
        self.users[id_] = set(ownedChunks)
        if not self.ids: heappush(self.ids, id_+1)
        return id_

    def leave(self, userID: int) -> None:
        for chunk in self.users[userID]:
            self.chunks[chunk].remove(userID)
        del self.users[userID]
        heappush(self.ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        tmp = list(self.chunks[chunkID])
        if not tmp: return []
        self.chunks[chunkID].add(userID)
        self.users[userID].add(chunkID)
        return sorted(tmp)

# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)