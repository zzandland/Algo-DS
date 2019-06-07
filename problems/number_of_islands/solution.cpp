class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0) return 0;
        int output = 0;
        int h = grid.size(), w = grid[0].size();
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (grid[i][j] == '1') {
                    ++output;
                    queue<pair<int, int>> q;
                    q.push(make_pair(i, j));
                    grid[i][j] = '0';
                    while (!q.empty()) {
                        pair<int, int> coord = q.front();
                        q.pop();
                        int y = coord.first;
                        int x = coord.second;
                        if (validCoord(y + 1, x, h, w) && grid[y + 1][x] == '1') {
                            grid[y + 1][x] = '0';
                            q.push({y + 1, x});
                        }
                        if (validCoord(y - 1, x, h ,w) && grid[y - 1][x] == '1') {
                            grid[y - 1][x] = '0';
                            q.push({y - 1, x});
                        }
                        if (validCoord(y, x + 1, h, w) && grid[y][x + 1] == '1') {
                            grid[y][x + 1] = '0';
                            q.push({y, x + 1});
                        }
                        if (validCoord(y, x - 1, h, w) && grid[y][x - 1] == '1') {
                            grid[y][x - 1] = '0';
                            q.push({y, x - 1});
                        }
                    }
                }
            }
        }
        return output;
    }
    
    bool validCoord(int y, int x, int h, int w) {
        return y >= 0 && y < h && x >= 0 && x < w;   
    }
};