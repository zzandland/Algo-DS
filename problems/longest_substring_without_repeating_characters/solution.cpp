class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int freq[128];
        for (int i = 0; i < 128; ++i) freq[i] = 0;
        
        int l, r, res;
        l = r = res = 0;
        while (r < s.size()) {
            freq[s[r]]++;
            while (freq[s[r]] > 1) {
                freq[s[l]]--;
                l++;
            }
            res = max(res, r - l + 1);
            r++;
        }
        return res;
    }
};