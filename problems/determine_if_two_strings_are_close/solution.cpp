class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) return false;
        int c1[27];
        int c2[27];
        for (int i = 0; i < 27; ++i) c1[i] = c2[i] = 0;
        
        for (int i = 0; i < word1.length(); ++i) {
            c1[word1[i] - 'a']++;
            c2[word2[i] - 'a']++;
        }
        
        for (int i = 0; i < 27; ++i) {
            if ((!c1[i] && c2[i]) || (c1[i] && !c2[i])) return false;
        }
        
        sort(c1, c1 + 27);
        sort(c2, c2 + 27);
        
        for (int i = 0; i < 27; ++i) if (c1[i] != c2[i]) return false;
        return true;
    }
};