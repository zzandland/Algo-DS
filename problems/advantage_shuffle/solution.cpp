class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        multiset<int> st(A.begin(), A.end());
        for (int i = 0; i < B.size(); ++i) {
            auto it = *st.rbegin() > B[i] ? st.upper_bound(B[i]) : st.begin();
            B[i] = *it;
            st.erase(it);
        }
        return B;
    }
};