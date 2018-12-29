class Solution {
  public int dominantIndex(int[] nums) {
    if (nums.length == 1) return 0;
    int biggest = 0, secondBiggest = 0, biggestIndex = -1, numsLen = nums.length;
    for (int i = 0; i < numsLen; i++) {
      if (secondBiggest < nums[i]) {
        if (biggest < nums[i]) {
          secondBiggest = biggest;
          biggest = nums[i];
          biggestIndex = i;
        } else {
          secondBiggest = nums[i];
        }
      }
    }
    return secondBiggest * 2 <= biggest ? biggestIndex : -1;
  }
}