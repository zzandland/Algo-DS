/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */

#include <iostream>
#include <sstream>

using namespace std;

// @lc code=start
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
// @lc code=end
