class Solution {
public:
    bool helper(int a, int b) {
        string sa = to_string(a), sb = to_string(b);
        int fa[10] = {0};
        int fb[10] = {0};
        for (char c : sa) ++fa[c - '0'];
        for (char c : sb) ++fb[c - '0'];
        for (int i = 0; i < 10; ++i) {
            if (fa[i] != fb[i]) return false;
        }
        return true;
    }
    
    bool reorderedPowerOf2(int N) {
        unordered_set<string> st;
        int n = 1;
        while (n <= pow(10, 9)) {
            if (helper(n, N)) return true;
            n *= 2;
        }
        return false;
    }
};