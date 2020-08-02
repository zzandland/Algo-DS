class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        vector<int> mns;
        
        int run = INT_MAX;
        for (int n: nums) {
            run = min(run, n);
            mns.push_back(run);
        }
        
        int mn;
        stack<int> st;
        for (int i = nums.size()-1; i >= 0; --i) {
            run = nums[i], mn = mns[i];
            if (run > mn) {
                while (!st.empty() && st.top() <= mn) st.pop();
                if (!st.empty() && st.top() < run) return true;
                st.push(run);
            }
        }
        return false;
    }
};