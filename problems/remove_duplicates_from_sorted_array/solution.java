class Solution {
  public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int pos = 1;
    int curr = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (curr != nums[i]) {
        nums[pos] = nums[i];
        curr = nums[i];
        pos++;
      }
    }
    return pos;
  }
}