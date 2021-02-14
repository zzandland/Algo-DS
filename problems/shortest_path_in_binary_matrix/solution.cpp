typedef pair<int, pair<int, int>> node;
inline size_t key(int i, int j) { return (size_t) i << 32 | (unsigned int) j; };

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int len = grid.size();
        if (!len || grid[0][0] == 1) return -1;
        queue<node> q;
        q.push({1, {0, 0}});
        
        unordered_set<size_t> seen;
        seen.emplace(key(0, 0));
        vector<pair<int, int>> dir = {{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}};
        
        while (!q.empty()) {
            auto [d, coord] = q.front();
            auto [y, x] = coord;
            if (y == len-1 && x == len-1) return d;
            q.pop();
            for (const auto &[r, c] : dir) {
                int ny = y + r, nx = x + c;
                if (0 <= ny && ny < len && 0 <= nx && nx < len && grid[ny][nx] == 0) {
                    if (!seen.count(key(ny, nx))) {
                        seen.emplace(key(ny, nx));
                        q.push({d+1, {ny, nx}});
                    }
                }
            }
        }
        return -1;
    }
};