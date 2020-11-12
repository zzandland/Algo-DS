/*
 * @lc app=leetcode id=31 lang=cpp
 *
 * [31] Next Permutation
 *
 * https://leetcode.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (30.48%)
 * Total Accepted:    237.9K
 * Total Submissions: 780.5K
 * Testcase Example:  '[1,2,3]'
 *
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers.
 *
 * If such arrangement is not possible, it must rearrange it as the lowest
 * possible order (ie, sorted in ascending order).
 *
 * The replacement must be in-place and use only constant extra memory.
 *
 * Here are some examples. Inputs are in the left-hand column and its
 * corresponding outputs are in the right-hand column.
 *
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 *
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  void nextPermutation(vector<int> &nums) {
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1])
      --i;
    if (i >= 0) {
      int j = bsearch(nums, i);
      swap(nums[i], nums[j]);
    }
    reverseDescending(nums, i + 1);
  }

  int bsearch(vector<int> &nums, int offset) {
    int target = nums[offset], left = offset + 1, right = nums.size() - 1;
    while (right > left) {
      int mid = left + (right - left) / 2;
      if (nums[mid] > target) {
        if (nums[mid + 1] <= target)
          return mid;
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }

  void reverseDescending(vector<int> &nums, int left) {
    int right = nums.size() - 1;
    while (right > left)
      swap(nums[left++], nums[right--]);
  }
};
