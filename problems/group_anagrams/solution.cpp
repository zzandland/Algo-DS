class Solution {
public:
  void CompareString(string str, map<vector<int>, vector<string>>& dic) {
    vector<int> count = LetterCount(str);
    if (dic.find(count) == dic.end()) {
      dic.insert({count, {str}});
    } else {
      dic[count].push_back(str);
    }
  }
  
  vector<int> LetterCount(string str) {
    vector<int> count(27);
    for (int i = 0; i < str.length(); i++) {
      count[(int)(str.at(i) - 'a')]++;
    }
    return count;
  }
  
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    map<vector<int>, vector<string>> dic;
    for (string str : strs) {
      CompareString(str, dic);
    }
    vector<vector<string>> output;
    for (auto it = dic.begin(); it != dic.end(); ++it) {
      output.push_back(it->second);
    }
    return output;
  }
  
};