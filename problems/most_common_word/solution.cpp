class Solution {
public:
  string mostCommonWord(string paragraph, vector<string>& banned) {
    unordered_set<string> ban_set(banned.begin(), banned.end());
    ban_set.insert("");
    unordered_map<string, int> word_map = getWordCounts(paragraph, ban_set);
    int largest = INT_MIN;
    string frequent = "";
    for (auto it = word_map.begin(); it != word_map.end(); ++it) {
      if (it->second > largest) {
        largest = it->second;
        frequent = it->first;
      }
    }
    return frequent;
  }
  
  unordered_map<string, int> getWordCounts(const string& s, const unordered_set<string>& ban_set) {
    unordered_map<string, int> word_map;
    unordered_set<char> stop_char = {' ', '\'', '!', '?', ',', ';', '.'};
    int i = 0;
    while (i < s.length()) {
      string tmp = "";      
      while (i < s.length() && stop_char.count(s[i]) == 0) {
        char c = s[i++];
        if ((int)c < 91) {
          c = (int)c + 32;
        }
        tmp += c;
      }
      if (ban_set.count(tmp) == 0)
        ++word_map[tmp];
      ++i;
    }
    return word_map;
  }
};