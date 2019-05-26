#include <list>
#include <bits/stdc++.h>

class Solution {
public:
  vector<string> reorderLogFiles(vector<string>& logs) {
    stable_sort(logs.begin(), logs.end(), [&](const string& s1, const string& s2) {
      int i1 = s1.find(' ') + 1, i2 = s2.find(' ') + 1;
      if (!isdigit(s1[i1]) && !isdigit(s2[i2])) {
        if (s1.substr(i1) == s2.substr(i2))
          return s1.substr(0, i1) < s2.substr(0, i2);
        else
          return s1.substr(i1) < s2.substr(i2);
      } else {
        if (!isdigit(s1[i1])) return true;
        return false;
      }
    });
    return logs;
  }
};