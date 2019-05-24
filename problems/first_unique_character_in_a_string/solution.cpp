class Solution {
public:
  int firstUniqChar(string s) {
    vector<int> c_map(26, 0);
    for (char c : s)
      ++c_map[c - 'a'];
    for (int i = 0; i < s.length(); ++i) {
      if (c_map[s[i] - 'a'] == 1) 
        return i;
    }
    return -1;
  }
};