/*
 * @lc app=leetcode id=47 lang=cpp
 *
 * [47] Permutations II
 *
 * https://leetcode.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (43.88%)
 * Total Accepted:    305.1K
 * Total Submissions: 695.2K
 * Testcase Example:  '[1,1,2]'
 *
 * <p>Given a collection of numbers that might contain duplicates, return all
 * possible unique permutations.</p>
 * 
 * <p><strong>Example:</strong></p>
 * 
 * <pre>
 * <strong>Input:</strong> [1,1,2]
 * <strong>Output:</strong>
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 * </pre>
 * 
 */
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
  vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> output;
    if (nums.size() == 0) {
      output.push_back(vector<int>());
      return output;
    }
    if (nums.size() == 1) {
      output.push_back(nums);
      return output;
    }
    vector<int> st;
    while (nums.size() > 1) {
      st.push_back(nums.back());
      nums.pop_back();
    }
    int out;
    set<vector<int>> prev_set;
    set<vector<int>> out_set;
    prev_set.insert(nums);
    while (!st.empty()) {
      out = st.back();
      st.pop_back();
      out_set.clear();
      for (auto it = prev_set.begin(); it != prev_set.end(); ++it) {
        vector<int> cpy = *it;
        for (int i = 0; i <= cpy.size(); ++i) {
          cpy.insert(cpy.begin() + i, out);
          out_set.insert(cpy);
          cpy.erase(cpy.begin() + i);
        }
      }
      prev_set = out_set;
    }
    for (auto it = out_set.begin(); it != out_set.end(); ++it) {
      vector<int> v = *it;
      output.push_back(v);
    }
    return output;
  }
};
