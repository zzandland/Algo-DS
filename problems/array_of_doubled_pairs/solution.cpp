class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        map<int, int> mp;
        for (int n : arr) ++mp[n];
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            int n = it->first;
            if (mp[n] == 0) continue;
            if (n < 0) {
                if (n % 2 != 0 || mp[n] > mp[n / 2]) {
                    return false;
                }
                mp[n / 2] -= mp[n];
                mp[n] = 0;
            } else {
                if (mp[n] > mp[n * 2]) {
                    return false;
                }
                mp[n * 2] -= mp[n];
                mp[n] = 0;
            }
        }
        return true;
    }
};