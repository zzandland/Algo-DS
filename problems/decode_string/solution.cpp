class Solution {
public:
    string decodeString(string s) {
        stringstream ss(s);
        return helper(ss);
    }
    
    string helper(stringstream &ss) {
        string tmp, res;
        char c;
        while (ss >> c) {
            if (c == ']') return res;
            if (isdigit(c)) {
                tmp.clear();
                while (isdigit(c)) {
                    tmp += c;
                    ss >> c;
                }
                int freq = stoi(tmp);
                tmp = helper(ss);
                for (int i = 0; i < freq; ++i) res += tmp;
            } else {
                res += c;
            }
        }
        return res;
    }
};