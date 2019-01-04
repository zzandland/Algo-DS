class Solution {
  public int arrayPairSum(int[] nums) {
    Arrays.sort(nums);
    int output = 0;
    for (int i = 0; i < nums.length; i += 2) {
      output += nums[i];
    }
    return output;
  }
}