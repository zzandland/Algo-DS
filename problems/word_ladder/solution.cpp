class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> st;
        for (string w : wordList) st.emplace(w);
        if (!st.count(endWord)) return 0;
        int res = 0;
        queue<string> q;
        q.emplace(beginWord);
        if (st.count(beginWord)) st.erase(beginWord);
        while (!q.empty()) {
            res++;
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                string t = q.front();
                if (t == endWord) return res;
                q.pop();
                for (int j = 0; j < beginWord.size(); ++j) {
                    for (int k = 0; k < 27; ++k) {
                        string tmp = t.substr(0, j) + (char)('a'+k) + t.substr(j + 1, beginWord.size()-j-1);
                        if (st.count(tmp)) {
                            st.erase(tmp);
                            q.emplace(tmp);
                        }
                    }
                }
            }
        }
        return 0;
    }
};