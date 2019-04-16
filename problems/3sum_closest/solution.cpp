class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
    Quicksort(nums, 0, nums.size() - 1);
    int closest_sum = 0;
    int diff = INT_MAX;
    for (size_t i = 0; i < nums.size() - 2; ++i) {
      int left = i + 1;
      int right = nums.size() - 1;
      int sub_target = target - nums[i];
      while (right > left) {
        int two_sum = nums[left] + nums[right];
        if (two_sum == sub_target) return nums[i] + two_sum;
        int curr_diff = std::abs(sub_target - two_sum);
        if (curr_diff < diff) {
          closest_sum = nums[i] + two_sum;
          diff = curr_diff;
        }         
        if (two_sum > sub_target) --right;
        else ++left;
      }
    }
    return closest_sum;
  }

 private:
  void Quicksort(std::vector<int>& nums, int left, int right) {
    if (right > left) {
      int pivot = GetPivot(nums, left, right);  
      Quicksort(nums, left, pivot - 1);
      Quicksort(nums, pivot + 1, right);
    }
  }

  int GetPivot(std::vector<int>& nums, int left, int right) {
    int i = left - 1;
    int p = nums[right];
    for (int j = left; j < right; ++j)
      if (nums[j] < p) std::swap(nums[++i], nums[j]);
    std::swap(nums[++i], nums[right]);
    return i;
  }

};