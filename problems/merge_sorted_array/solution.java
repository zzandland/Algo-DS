class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    if (n == 0) return;
    if (m == 0) {
      copy(0, nums1, nums2);
      return;
    } 
    for (int i = 0; i < nums1.length; i++) {
      if (i >= m) {
        copy(i, nums1, nums2);
        return; 
      }
      if (nums1[i] > nums2[0]) {
        int temp = nums1[i];
        nums1[i] = nums2[0];
        nums2[0] = temp;
        sort(nums2);
      } 
    }
  }
  
  private void copy(int offset, int[] nums1, int[] nums2) {
    for (int i = 0; offset < nums1.length; i++, offset++) {
      nums1[offset] = nums2[i];
    }
  }
  
  private void sort(int[] nums) {
    for (int i = 0; i < nums.length - 1; i++) {
      if (nums[i] > nums[i + 1]) {
        int temp = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = temp;
      } else {
        break;
      }
    }
  }
}