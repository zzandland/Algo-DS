class Solution {
public:
    int scoreOfParentheses(string S) {
        queue<char> q;
        for (char c : S) q.push(c);
        return dfs(q);
    }
    
    int dfs(queue<char> &q) {
        int res, tmp;
        bool open = false;
        res = tmp = 0;
        char c;
        while (!q.empty() && (open || q.front() == '(')) {
            c = q.front();
            if (c == '(' && open) {
                tmp += dfs(q);
            } else {
                q.pop();
                if (c == ')') {
                    open = false;
                    res += (tmp ? tmp * 2 : 1);
                    tmp = 0;
                } else if (c == '(') {
                    open = true;
                }
            }
        }
        return res;
    }
};