class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }
        int l = 0;
        vector<int> res;
        for (int i = 0; i < nums1.size() && l < nums2.size(); ++i) {
            int r = nums2.size();
            while (l < r) {
                int m = l + (r - l) / 2;
                if (nums2[m] < nums1[i]) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            if (l < nums2.size() && nums2[l] == nums1[i]) {
                while (l < nums2.size() && i < nums1.size() && nums2[l] == nums1[i]) {
                    res.push_back(nums1[i]);
                    ++i, ++l;
                }
                --i;
            }
        }
        return res;
    }
};