class Solution {
public:
    pair<int, int> directions[4];
    Solution(): directions{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {}
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (!image.size()) return image;
        int m = image.size(), n = image[0].size();
        if (image[sr][sc] != newColor) {
            int color = image[sr][sc];
            image[sr][sc] = newColor;
            queue<pair<int, int>> q;
            q.emplace(sr, sc);
            while (!q.empty()) {
                auto [y, x] = q.front();
                q.pop();
                for (auto [r, c]: directions) {
                    int ny = y+r, nx = x+c;
                    if (0 <= ny && ny < m && 0 <= nx && nx < n && image[ny][nx] == color) {
                        image[ny][nx] = newColor;
                        q.emplace(ny, nx);
                    }
                }
            }
        }
        return image;
    }
};