class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int l = 0, r = 0, mx = 1<<31;
        while (l < nums.length) {
            if (nums[l] <= mx) {
                while (r < nums.length && nums[r] <= mx) r++;
                if (r == nums.length) return l;
                nums[l] = nums[r];
            }
            mx = nums[l++];
        }
        return l;
    }
}