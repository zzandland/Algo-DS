class Solution {
public:
    string removeDuplicates(string s, int k) {
        bool found;
        do {
            found = false;
            string t;
            char prev = ' ';
            int cnt = 0;
            for (char c : s) {
                if (c != prev) {
                    for (int i = 0; i < cnt; ++i) t += prev;
                    prev = c;
                    cnt = 1;
                } else {
                    ++cnt;
                } 
                if (cnt == k) {
                    prev = ' ';
                    cnt = 0;
                    found = true;
                }
            }
            for (int i = 0; i < cnt; ++i) t += prev;
            s = t;
        } while (found);
        return s;
    }
};