class Solution:
    def floodFill(self, image: List[List[int]], 
                  sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []
        R, C, dir_= len(image), len(image[0]), ((1, 0), (-1, 0), (0, 1), (0, -1))
        seen, st, prev = [[False]*C for _ in range(R)], [], image[sr][sc]
        if prev != newColor:
            st.append((sr, sc))
            seen[sr][sc] = True
        while st:
            r, c = st.pop()
            image[r][c] = newColor
            for y, x in dir_:
                nr, nc = r+y, c+x
                if (0 <= nr < R and 0 <= nc < C and
                    not seen[nr][nc] and image[nr][nc] == prev):
                    seen[nr][nc] = True
                    st.append((nr, nc))
        return image