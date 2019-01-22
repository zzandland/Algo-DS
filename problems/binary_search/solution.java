class Solution {
  public int search(int[] nums, int target) {
    if (nums == null || nums.length == 0) return -1;
    int left = 0;
    int right = nums.length - 1;
    int mid;
    while (right > left + 1) {
      mid = left + (right - left) / 2;
      if (nums[mid] == target) return mid;
      if (mid - 1 >= 0 && nums[mid - 1] == target) return mid - 1;
      if (mid + 1 < nums.length && nums[mid + 1] == target) return mid + 1;
      if (nums[mid] > target) right = mid;
      else left = mid;
    }  
    if (nums[left] == target) return left;
    if (nums[right] == target) return right;
    return -1;
  }
}