#include <iostream>
#include <vector>

using namespace std;

/*
 * @lc app=leetcode id=32 lang=cpp
 *
 * [32] Longest Valid Parentheses
 *
 * https://leetcode.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (25.50%)
 * Total Accepted:    190.6K
 * Total Submissions: 747.3K
 * Testcase Example:  '"(()"'
 *
 * Given a string containing just the characters '(' and ')', find the length
 * of the longest valid (well-formed) parentheses substring.
 *
 * Example 1:
 *
 *
 * Input: "(()"
 * Output: 2
 * Explanation: The longest valid parentheses substring is "()"
 *
 *
 * Example 2:
 *
 *
 * Input: ")()())"
 * Output: 4
 * Explanation: The longest valid parentheses substring is "()()"
 *
 *
 */
class Solution {
public:
  int longestValidParentheses(string s) {
    int len = s.length();
    vector<vector<vector<int>>> dp(len,
                                   vector<vector<int>>(len, vector<int>(len)));
    return longestValidParentheses(s, 0, 0, 0, dp);
  }

  int longestValidParentheses(string s, size_t i, int len, int count,
                              vector<vector<vector<int>>> &dp) {
    if (i == s.length())
      return count == 0 ? len : 0;
    if (count < 0)
      return 0;
    if (!dp[i][len][count]) {
      int output = 0;
      if (count == 0 && i > 0)
        output = len;
      int next =
          (s[i] == '(')
              ? longestValidParentheses(s, i + 1, len + 1, count + 1, dp)
              : longestValidParentheses(s, i + 1, len + 1, count - 1, dp);
      dp[i][len][count] =
          max(output, max(next, longestValidParentheses(s, i + 1, 0, 0, dp)));
    }
    return dp[i][len][count];
  }
};
