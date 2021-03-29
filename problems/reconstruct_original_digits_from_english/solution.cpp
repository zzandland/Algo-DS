class Solution {
public:
    string originalDigits(string s) {
        // 0z  2w 4u 6x 5f 7v 1o 3r 9n 8
        vector<int> freq(26);
        for (const char c : s) ++freq[c - 'a'];
        vector<int> order{0, 2, 4, 6, 5, 7, 1, 3, 9, 8};
        vector<int> numFreq(10);
        for (int n : order) numFreq[n] = useChars(n, freq);
        string res;
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < numFreq[i]; ++j) res += to_string(i);
        }
        return res;
    }
    
    int useChars(int n, vector<int> &freq) {
        auto [k, s] = dic[n];
        int res = 0;
        while (freq[k - 'a'] > 0) {
            ++res;
            for (const char c : s) --freq[c - 'a'];
        }
        return res;
    } 

private:
    unordered_map<int, pair<char, string>> dic{
        {0, {'z', "zero"}}, {1, {'o', "one"}}, {2, {'w', "two"}},
        {3, {'r', "three"}}, {4, {'u', "four"}}, {5, {'f', "five"}},
        {6, {'x', "six"}}, {7, {'v', "seven"}}, {8, {'e', "eight"}},
        {9, {'n', "nine"}}
    };
};