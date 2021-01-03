class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        int map[101];
        for (int i = 0; i < 101; ++i) map[i] = -1;
        for (int i = 0; i < pieces.size(); ++i) map[pieces[i][0]] = i;
        for (int i = 0; i < arr.size();) {
            int pos = map[arr[i]];
            if (pos == -1) return false;
            for (int j = 0; j < pieces[pos].size(); ++i, ++j) {
                if (arr[i] != pieces[pos][j]) return false;
            }
        }
        return true;
    }
};