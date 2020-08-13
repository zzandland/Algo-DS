class CombinationIterator {
public:
    vector<int> st;
    int len;
    string s;
    bool end;
    
    CombinationIterator(string characters, int combinationLength)
        : len(combinationLength), s(characters), end(false) {
        for (int i = 0; i < len; ++i) st.push_back(i);
    }
    
    string next() {
        ostringstream oss;
        for (int idx: st) oss << s[idx];
        
        for (int i = 0; i < len; ++i) {
            if (st[st.size()-1] == s.size()-i-1) st.pop_back();
            else break;
        }
        
        if (st.empty()) end = true;
        else {
            st[st.size()-1] += 1;
            while (st.size() < len) st.push_back(st[st.size()-1] + 1);
        }
        
        return oss.str();
    }
    
    bool hasNext() {
        return !end;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */