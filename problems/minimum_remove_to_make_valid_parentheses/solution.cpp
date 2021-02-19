class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int cnt, mn;
        cnt = mn = 0;
        for (char &c : s) {
            cnt += (c == '(');
            cnt -= (c == ')');
            if (cnt < mn) mn = cnt, c = '*';
        }
        
        int opens = cnt - mn;
        for (auto it = s.rbegin(); opens; ++it) {
            if (*it == '(') *it = '*', opens--;
        }
        
        string res;
        for (char &c : s) {
            if (c != '*') res += c;
        }
        return res;
    }
};