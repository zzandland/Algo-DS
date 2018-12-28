class Solution {
    public int pivotIndex(int[] nums) {
      int sum = 0, total = 0;
      int numsLen = nums.length;
      for (int num : nums) total += num;
      for (int i = 0; i < numsLen; i++) {
        if (total == sum * 2 + nums[i]) {
          return i;
        }
        sum += nums[i];
      }
      return -1;
    }
}