class Solution {
public:
    unordered_map<int, int> coord2group, group2size;
    vector<vector<int>> grid;
    vector<vector<bool>> cache;
    vector<int> dirs;
    
    Solution(): dirs({-1, 0, 1, 0, -1}) {}
    
    bool validCoord(int y, int x, int R, int C) {
        return 0 <= y && y < R && 0 <= x && x < C;
    }
    
    void explore(int y, int x, int group) {
        int R = grid.size(), C = grid[0].size();
        int coord = y * C + x;
        coord2group[coord] = group;
        ++group2size[group];
        for (int i = 0; i < dirs.size() - 1; ++i) {
            int ny = y + dirs[i], nx = x + dirs[i+1];
            if (validCoord(ny, nx, R, C)) {
                if (!cache[ny][nx] && grid[ny][nx] == 1) {
                    cache[ny][nx] = true;
                    explore(ny, nx, group);
                }
            }
        }
    }
    
    int largestIsland(vector<vector<int>>& grid) {
        int R = grid.size(), C = grid[0].size();
        // map: coord2group
        // map: group2size
        this->grid = grid;
        this->cache = vector<vector<bool>>(R, vector<bool>(C, false));
        // DFS or BFS
        int group = 0;
        for (int y = 0; y < R; ++y) {
            for (int x = 0; x < C; ++x) {
                if (!cache[y][x] && grid[y][x] == 1) {
                    cache[y][x] = true;
                    explore(y, x, group++);
                }
            }
        }
        
        int res = 0;
        for (auto it = group2size.begin(); it != group2size.end(); ++it) {
            res = max(res, it->second);
        }
        
        // walk on ocean and check four sides for biggest island if joined
        for (int y = 0; y < R; ++y) {
            for (int x = 0; x < C; ++x) {
                if (grid[y][x] == 0) {
                    int tmp = 1;
                    unordered_set<int> seen;
                    for (int i = 0; i < dirs.size() - 1; ++i) {
                        int ny = y + dirs[i], nx = x + dirs[i+1];
                        if (validCoord(ny, nx, R, C) && grid[ny][nx] == 1) {
                            int coord = ny * C + nx, group = coord2group[coord];
                            if (!seen.count(group)) {
                                seen.insert(group);
                                tmp += group2size[group];
                            }
                        }
                    }
                    res = max(res, tmp);
                }
            }
        }
        return res;
    }
};