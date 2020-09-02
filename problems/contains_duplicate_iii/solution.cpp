class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k <= 0 || t < 0) return false;
        map<int, int> seen;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k && --seen[nums[i-k-1]] == 0) seen.erase(nums[i-k-1]);
            if (seen.count(nums[i])) return true;
            auto up = seen.upper_bound(nums[i]);
            if (up != seen.end() && up->first - t <= nums[i]) return true;  
            auto down = seen.lower_bound(nums[i]);
            if (down != seen.begin()) {
                if ((--down)->first + t >= nums[i]) return true;
            }
            seen[nums[i]]++;
        }
        return false;
    }
};