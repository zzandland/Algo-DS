class Solution {
public:
    bool detectCapitalUse(string word) {
        return (
            all_of(word.begin(), word.end(), [](char c) { return isupper(c); }) ||
            all_of(word.begin(), word.end(), [](char c) { return islower(c); }) ||
            (isupper(word[0]) && all_of(word.begin()+1, word.end(), [](char c) { return islower(c); }))
        );
    }
};