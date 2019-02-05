class Solution {
  public int maxSubArray(int[] nums) {
    int L, R, maxL, maxR, curr, max;
    L = R = maxL = maxR = curr = 0;
    max = Integer.MIN_VALUE;
    for (; R < nums.length; R++) {
      curr += nums[R];
      if (nums[R] > curr) {
        L = R;
        curr = nums[R];
        if (curr > max) maxL = R;
      }
      if (curr > max) {
        max = curr;
        maxR = R;
      } 
    }
    return max;
  }
}