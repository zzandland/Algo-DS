#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

/*
 * @lc app=leetcode id=18 lang=cpp
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (30.15%)
 * Total Accepted:    226K
 * Total Submissions: 747.7K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate quadruplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */
class Solution {
public:
  std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
    std::set<std::vector<int>> output_set;
    if (nums.size() >= 4) {
      quickSort(nums, 0, nums.size() - 1);
      for (size_t i = 0; i < nums.size() - 3; ++i) {
        for (size_t j = i + 1; j < nums.size() - 2; ++j) {
          int remainder = target - nums[i] - nums[j];
          int left = j + 1;
          int right = nums.size() - 1;
          while (right > left) {
            int sum = nums[left] + nums[right];
            if (sum == remainder) {
              std::vector<int> s = {nums[i], nums[j], nums[left], nums[right]};
              output_set.insert(s);
              --right;
            } else if (sum > remainder) {
              --right;
            } else {
              ++left;
            }
          }
        }
      }
    }
    std::vector<std::vector<int>> output;
    output.insert(output.end(), output_set.begin(), output_set.end());
    return output;
  };

  void quickSort(std::vector<int>& nums, int left, int right) {
    if (right > left) {
      int pivot = partition(nums, left, right);
      quickSort(nums, left, pivot - 1);
      quickSort(nums, pivot + 1, right);
    }
  };

  int partition(std::vector<int>& nums, int left, int right) {
    int i = left - 1;
    for (int j = left; j < right; ++j)
      if (nums[j] < nums[right]) std::swap(nums[j], nums[++i]);
    std::swap(nums[++i], nums[right]);
    return i;
  };
};
