class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.size(); ++i) {
            if (j < i) j = i;
            while (j < nums.size() && nums[j] == val) j++;
            if (j == nums.size()) break;
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        return i;
    }
};