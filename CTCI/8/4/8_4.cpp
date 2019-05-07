#include <iostream>
#include <vector>

std::vector<std::vector<int>> PowerSet(std::vector<int>& nums);
void PowerSet(std::vector<int>& nums, std::vector<int>& subset,
              std::vector<std::vector<int>>& output, size_t i);

int main(void) {
  std::vector<int> nums = {1,2,3,4,5};
  std::vector<std::vector<int>> output = PowerSet(nums);
  for (std::vector<int> subset : output) {
    for (int n : subset) {
      std::cout << n << " ";
    }
    std::cout << std::endl;
  }
  return 0;
}

std::vector<std::vector<int>> PowerSet(std::vector<int>& nums) {
  std::vector<std::vector<int>> output;
  std::vector<int> subset;
  PowerSet(nums, subset, output, 0);
  return output;
}

void PowerSet(std::vector<int>& nums, std::vector<int>& subset,
              std::vector<std::vector<int>>& output, size_t i) {
  if (i == nums.size()) {
    std::vector<int> cpy(subset);
    output.push_back(cpy);
    return;
  }
  subset.push_back(nums[i]);
  PowerSet(nums, subset, output, i + 1);
  subset.pop_back();
  PowerSet(nums, subset, output, i + 1);
}
