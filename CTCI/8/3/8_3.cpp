#include <iostream>
#include <vector>

int MagicNumber(std::vector<int>& nums);
int MagicNumber(std::vector<int>& nums, size_t left, size_t right);

int main(void)
{
  std::vector<int> n = {-10,-5,2,2,2,3,4,7,9,12,13};
  std::cout << MagicNumber(n);
  return 0;
}

int MagicNumber(std::vector<int>& nums) {
  return MagicNumber(nums, 0, nums.size() - 1);
}

int MagicNumber(std::vector<int>& nums, size_t left, size_t right) {
  if (right < left) return -1;
  int mid = left + (right - left) / 2;
  if (nums[mid] == (int)mid) return nums[mid];
  if (nums[mid] > mid)
    return MagicNumber(nums, left, mid - 1);
  else
    return MagicNumber(nums, left + 1, right);
}
