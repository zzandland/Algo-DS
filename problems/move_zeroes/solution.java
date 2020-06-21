class Solution {
    public void moveZeroes(int[] nums) {
        for (int i = 0, j = 0; i < nums.length; i++, j++) {
            if (nums[i] == 0) {
                while (j < nums.length && nums[j] == 0) j++;
                if (j == nums.length) return;
                nums[i] = nums[j];
                nums[j] = 0;
            }
        }
    }
}