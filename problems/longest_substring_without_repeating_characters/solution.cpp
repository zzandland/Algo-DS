#include <vector>

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    vector<int> c_map(128, -1);
    int l, r, longest;
    l = -1; r = 0, longest = 0;
    for (; r < (int)s.length(); ++r) {
      int c = s[r];
      if (c_map[c] != -1)
        l = max(l, c_map[c]);
      c_map[c] = r;
      longest = max(longest, r - l);
    }
    return longest;
  }
  
  int lengthOfLongestSubstring(string s, int l, int r, set<char>& c_set) {
    if (r == (int)s.length()) return 0;
    char c = s[r];
    if (c_set.find(c) == c_set.end())
      c_set.insert(c);
    else 
      while (s[++l] != c) c_set.erase(s[l]);
    return max(r - l, lengthOfLongestSubstring(s, l, r + 1, c_set));
  }
};