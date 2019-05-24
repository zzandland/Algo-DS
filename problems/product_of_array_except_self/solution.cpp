class Solution {
public:
  vector<int> productExceptSelf(vector<int>& nums) {
    int len = nums.size();
    vector<int> output(len);
    int sum = 1;
    output[0] = sum;
    for (int i = 1; i < len; ++i) {
      sum *= nums[i - 1];
      output[i] = sum;
    }
    sum = 1;
    for (int j = len - 2; j >= 0; --j) {
      sum *= nums[j + 1];
      output[j] *= sum;
    }
    return output;
  }
};