class Solution {
  public int minSubArrayLen(int s, int[] nums) {
    if (nums.length == 0) return 0; 
    int output = nums.length + 1, sum = 0, left = 0;
    for (int i = 0; i < nums.length; i++) {
      sum += nums[i];
      while (sum >= s) {
        output = Math.min(output, i - left + 1);
        sum -= nums[left++];
      }
    }
    return output == nums.length + 1 ? 0 : output;
  }    
}