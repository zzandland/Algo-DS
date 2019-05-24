#include <set>

class Solution {
public:
  int missingNumber(vector<int>& nums) {
    int arr_sum = 0;
    int greatest = INT_MIN;
    bool zero = false;
    for (int num : nums) {
      if (num == 0) zero = true;
      arr_sum += num;
      greatest = max(greatest, num);
    }
    int sum = getIncrementalSum(greatest);
    return (zero && sum == arr_sum) ? greatest + 1 : sum - arr_sum;
  }
  
  int getIncrementalSum(int num) {
    int output = 0;
    for (int i = 1; i <= num; ++i)
      output += i;
    return output;
  }
};