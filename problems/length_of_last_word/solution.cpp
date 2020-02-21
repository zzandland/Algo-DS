class Solution {
public:
  int lengthOfLastWord(string s) {
    char delim = ' ';
    size_t prev, curr = 0;
    istringstream ss(s);
    string word;
    do {
      ss >> word;
    } while (ss);
    return word.length();
  }
};