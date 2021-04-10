class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int map[26];
        for (int i = 0; i < order.length(); ++i) map[order[i] - 'a'] = i;
        for (int i = 0; i < words.size() - 1; ++i) {
            if (!compare(words[i], words[i+1], map)) return false;
        }
        return true;
    }
    
    bool compare(const string& a, const string& b, int* map) {
        bool same = true;
        for (int i = 0; i < min(a.length(), b.length()); ++i) {
            int aa = a[i] - 'a', bb = b[i] - 'a';
            if (map[aa] != map[bb]) return map[aa] < map[bb];
        }
        return a.length() <= b.length();
    }
};