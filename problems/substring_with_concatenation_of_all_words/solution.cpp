class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        int wordSize = words[0].length();
        multiset<string> st;
        for (string &s : words) st.insert(s);
        
        for (int i = 0; i < s.length(); ++i) {
            if (s.length() - i >= st.size() * wordSize) {
                multiset<string> cpy = st;
                string tmp;
                for (int j = i; j < s.length(); ++j) {
                    tmp += s[j];
                    if ((j - i) % wordSize == wordSize - 1) {
                        if (!cpy.count(tmp)) break;
                        cpy.erase(cpy.find(tmp));
                        tmp = "";
                    }
                    if (cpy.empty()) {
                        res.push_back(i);  
                        break;
                    } 
                }
            }
        }
        
        return res;
    }
};