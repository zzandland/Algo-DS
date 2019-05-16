class Solution {
public:
  string generateCharCount(string s) {
    vector<int> counts(27);
    for (char c : s)  
      counts[c - 'a']++;
    string output = "";
    for (int i : counts)
      output += i - '0';
    return output;
  }
  
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> charMap;
    for (string s : strs) {
      charMap[generateCharCount(s)].push_back(s);
    }
    vector<vector<string>> output;
    for (auto it = charMap.begin(); it != charMap.end(); ++it)
      output.push_back(it->second);
    return output;
  }
};