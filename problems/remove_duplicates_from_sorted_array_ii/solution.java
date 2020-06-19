class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int l = 1, r = 1, mx = nums[0];
        boolean seen = false;
        while (l < nums.length) {
            if (mx == nums[r] && !seen) {
                while (r < nums.length && nums[r] < mx) r++;
                seen = true;
            } else {
                while (r < nums.length && nums[r] <= mx) r++;
                if (r >= nums.length) return l;
                mx = nums[r];
                seen = false;
            }
            nums[l++] = nums[r++];
            if (r >= nums.length) return l;
        }
        return l;
    }
}