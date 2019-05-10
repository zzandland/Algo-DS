class Solution {
public:
  int romanToInt(string s) {
    int output = 0;
    map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    for (int i = 0; i < (int)s.length(); ++i) {
      if (i + 1 < (int)s.length() && roman[s[i + 1]] > roman[s[i]])
        output -= roman[s[i]];
      else
        output += roman[s[i]];
    }
    return output;
  }
};