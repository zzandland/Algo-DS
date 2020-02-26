/*
 * @lc app=leetcode id=60 lang=cpp
 *
 * [60] Permutation Sequence
 *
 * https://leetcode.com/problems/permutation-sequence/description/
 *
 * algorithms
 * Medium (35.23%)
 * Likes:    1169
 * Dislikes: 286
 * Total Accepted:    164.6K
 * Total Submissions: 466.8K
 * Testcase Example:  '3\n3'
 *
 * The set [1,2,3,...,n] contains a total of n! unique permutations.
 * 
 * By listing and labeling all of the permutations in order, we get the
 * following sequence for n = 3:
 * 
 * 
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * 
 * 
 * Given n and k, return the k^th permutation sequence.
 * 
 * Note:
 * 
 * 
 * Given n will be between 1 and 9 inclusive.
 * Given k will be between 1 and n! inclusive.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 3, k = 3
 * Output: "213"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 4, k = 9
 * Output: "2314"
 * 
 * 
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
  int factorial(int n) {
    if (n == 0) {
      return 0;
    }
    if (n == 1) {
      return 1;
    }
    int output = 1;
    for (int i = 2; i <= n; ++i) {
      output *= i;
    }
    return output;
  }

  int getIndex(int k, int div) {
    int output = 0;
    if (k == 0) {
      return -1;
    }
    while (k > div) {
      ++output;
      k -= div;
    }
    return output;
  }

  string getPermutation(int n, int k) {
    string output = "";
    vector<int> st;
    for (int i = 1; i <= n; ++i) {
      st.push_back(i);
    }
    int div, index;
    while (n > 0) {
      if (n == 1) {
        index = 0;
      } else {
        div = factorial(n - 1);
        index = getIndex(k, div);
        if (index == -1) {
          index = st.size() - 1;
        }
        k %= div;
      }
      --n;
      output += to_string(st[index]);
      st.erase(st.begin() + index);
    }
    return output;
  }
};
// @lc code=end
