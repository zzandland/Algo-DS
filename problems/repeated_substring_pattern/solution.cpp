/*
 * @lc app=leetcode id=459 lang=cpp
 *
 * [459] Repeated Substring Pattern
 *
 * https://leetcode.com/problems/repeated-substring-pattern/description/
 *
 * algorithms
 * Easy (39.90%)
 * Total Accepted:    80.1K
 * Total Submissions: 200.7K
 * Testcase Example:  '"abab"'
 *
 * Given a non-empty string check if it can be constructed by taking a
 * substring of it and appending multiple copies of the substring together. You
 * may assume the given string consists of lowercase English letters only and
 * its length will not exceed 10000.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "abab"
 * Output: True
 * Explanation: It's the substring "ab" twice.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "aba"
 * Output: False
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "abcabcabcabc"
 * Output: True
 * Explanation: It's the substring "abc" four times. (And the substring
 * "abcabc" twice.)
 * 
 * 
 */
class Solution {
public:
  bool repeatedSubstringPattern(string s) {
    int len = s.length();
    if (len == 1) return false;
    if (allSameChar(s)) return true;
    for (int i = 2; i <= len / 2; ++i) {
      if (len % i == 0 && len / i > 1) {
        if (checkDivided(s, i)) return true;
      }
    }
    return false;
  }

  bool allSameChar(string s) {
    for (int i = 0; i < s.length(); ++i) {
      if (s[i] != s[0]) return false;
    }
    return true;
  }

  bool checkDivided(string s, int divisor) {
    int dividend = s.length() / divisor;
    for (int i = 0; i < dividend; ++i) {
      for (int j = i + dividend; j < s.length(); j += dividend) {
        if (s[j] != s[i]) return false;
      }
    }
    return true;
  }
};
