class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int i, j;
        i = j = 0;
        while (j < popped.size()) {
            if (!st.empty() && st.top() == popped[j]) {
                st.pop();
                j++;
            } else {
                if (i == pushed.size()) return false;
                st.push(pushed[i++]);
            }
        }
        return true;
    }
};