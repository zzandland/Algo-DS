/*
 * @lc app=leetcode id=39 lang=cpp
 *
 * [39] Combination Sum
 *
 * https://leetcode.com/problems/combination-sum/description/
 *
 * algorithms
 * Medium (48.54%)
 * Total Accepted:    343.4K
 * Total Submissions: 707.2K
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * Given a set of candidate numbers (candidates) (without duplicates) and a
 * target number (target), find all unique combinations in candidates where the
 * candidate numbers sums to target.
 *
 * The same repeated number may be chosen from candidates unlimited number of
 * times.
 *
 * Note:
 *
 *
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 *
 *
 * Example 1:
 *
 *
 * Input: candidates = [2,3,6,7], target = 7,
 * A solution set is:
 * [
 * ⁠ [7],
 * ⁠ [2,2,3]
 * ]
 *
 *
 * Example 2:
 *
 *
 * Input: candidates = [2,3,5], target = 8,
 * A solution set is:
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
 * ]
 *
 *
 */
class Solution {
public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<vector<int>> output;
    vector<int> v;
    recurse(candidates, v, target, 0, 0, output);
    return output;
  }

  void recurse(vector<int> &candidates, vector<int> &v, int target, int i,
               int sum, vector<vector<int>> &output) {
    if (i >= candidates.size())
      return;
    if (sum == target) {
      vector<int> tmp(v.begin(), v.end());
      output.push_back(tmp);
      return;
    }
    if (sum + candidates[i] <= target) {
      v.push_back(candidates[i]);
      recurse(candidates, v, target, i, sum + candidates[i], output);
      v.pop_back();
    }
    recurse(candidates, v, target, i + 1, sum, output);
  }
};
