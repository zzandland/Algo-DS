class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int y, x, d, ny, nx;
        y = x = d = 0;
        int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        for (int i = 1; i <= n*n; ++i) {
            res[y][x] = i;
            ny = y + dir[d][0];
            nx = x + dir[d][1];
            if (0 > ny || ny >= n || 0 > nx || nx >= n || res[ny][nx] != 0) {
                d = (d+1) % 4;
                ny = y + dir[d][0];
                nx = x + dir[d][1];
            }
            y = ny;
            x = nx;
        }
        
        return res;
    }
}