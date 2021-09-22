class Solution {
public:
    int maxLength(vector<string>& arr) {
        return dfs(arr, 0, 0);
    }
    
    uint32_t dfs(vector<string>& arr, size_t i, uint32_t bitmap) {
        if (arr.size() == i) {
            uint32_t cpy = bitmap, cnt = 0;
            while (cpy > 0) {
                if ((cpy & 1) == 1) ++cnt;
                cpy >>= 1;
            }
            return cnt;
        }
        uint32_t n = 0, res = 0;
        for (char c : arr[i]) {
            uint32_t idx = 1 << (c - 'a');
            if ((n & idx) != 0) {
                n = 0;
                break;
            }
            n |= idx;
        }
        if ((n & bitmap) == 0 && n != 0) {
            res = max(res, dfs(arr, i + 1, bitmap | n));
        }
        return max(res, dfs(arr, i + 1, bitmap));
    }
};