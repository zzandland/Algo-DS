class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        seen, st = set([0]), [0]
        while st:
            n = st.pop()
            for nn in rooms[n]:
                if nn not in seen:
                    seen.add(nn)
                    st.append(nn)
        return len(seen) == N