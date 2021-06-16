class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        stack<pair<string, int>> st;
        st.push({"", 0});
        while (!st.empty()) {
            auto [tmp, cur] = st.top();
            st.pop();
            if (cur >= 0) {
                if (tmp.length() == n * 2) {
                    if (cur == 0)
                        res.push_back(tmp);
                } else {
                    st.push({tmp + '(', cur + 1});
                    st.push({tmp + ')', cur - 1});
                }
            }
        }
        return res;
    }
};