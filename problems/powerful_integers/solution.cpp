class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        vector<int> res;
        unordered_set<int> st;
        for (int i = 0; pow(x, i) + 1 <= bound; ++i) {
            if (x == 1 && i > 0) break;
            for (int j = 0; pow(x, i) + pow(y, j) <= bound; ++j) {
                if (y == 1 && j > 0) break;
                st.insert(pow(x, i) + pow(y, j));
            }
        }
        if (x != y) {
            for (int i = 0; pow(y, i) + 1 <= bound; ++i) {
                if (y == 1 && i > 0) break;
                for (int j = 0; pow(y, i) + pow(x, j) <= bound; ++j) {
                    if (x == 1 && j > 0) break;
                    st.insert(pow(y, i) + pow(x, j));
                }
            }
        }
        res.insert(res.end(), st.begin(), st.end());
        return res;
    }
};