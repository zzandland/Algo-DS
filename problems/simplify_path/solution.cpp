class Solution {
public:
    string simplifyPath(string path) {
        string res, tmp;
        vector<string> st;
        stringstream ss(path);
        
        while (getline(ss, tmp, '/')) {
            if (tmp == "..") { 
                if (!st.empty()) st.pop_back();
            } else if (tmp != "." && !tmp.empty()) {
                st.push_back(tmp);
            }
        }
        
        for (string s : st) res += '/' + s;
        return res.empty() ? "/" : res;
    }
};