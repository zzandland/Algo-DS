/*
 * @lc app=leetcode id=40 lang=cpp
 *
 * [40] Combination Sum II
 *
 * https://leetcode.com/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (41.63%)
 * Total Accepted:    221.4K
 * Total Submissions: 531.8K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * Given a collection of candidate numbers (candidates) and a target number
 * (target), find all unique combinations in candidates where the candidate
 * numbers sums to target.
 *
 * Each number in candidates may only be used once in the combination.
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
 * Input: candidates = [10,1,2,7,6,1,5], target = 8,
 * A solution set is:
 * [
 * ⁠ [1, 7],
 * ⁠ [1, 2, 5],
 * ⁠ [2, 6],
 * ⁠ [1, 1, 6]
 * ]
 *
 *
 * Example 2:
 *
 *
 * Input: candidates = [2,5,2,1,2], target = 5,
 * A solution set is:
 * [
 * [1,2,2],
 * [5]
 * ]
 *
 *
 */
class Solution {
public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    set<vector<int>> output;
    vector<int> v;
    recurse(output, v, candidates, 0, target, 0);
    vector<vector<int>> o_vector(output.begin(), output.end());
    return o_vector;
  }

  void recurse(set<vector<int>> &output, vector<int> &v,
               vector<int> &candidates, int i, int target, int sum) {
    if (target == sum) {
      vector<int> tmp(v.begin(), v.end());
      sort(tmp.begin(), tmp.end());
      output.insert(tmp);
      return;
    }
    if (i >= candidates.size())
      return;
    if (sum + candidates[i] <= target) {
      v.push_back(candidates[i]);
      recurse(output, v, candidates, i + 1, target, sum + candidates[i]);
      v.pop_back();
    }
    recurse(output, v, candidates, i + 1, target, sum);
  }
};
