class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exacts(wordlist.begin(), wordlist.end());
        unordered_map<string, string> capitals;
        unordered_map<string, string> vowels;
        
        for (const string& word : wordlist) {
            const string lowered = toLowerStr(word);
            if (!capitals.count(lowered)) capitals[lowered] = word;
            const string voweled = toVowelStr(word);
            if (!vowels.count(voweled)) vowels[voweled] = word;
        }
        
        
        vector<string> res;
        for (const string& query : queries) {
            string tmp = "";
            if (exacts.count(query)) {
                tmp = query;
            } else {
                const string lowered = toLowerStr(query);
                if (capitals.count(lowered)) {
                    tmp = capitals[lowered];
                } else {
                    const string voweled = toVowelStr(query);
                    if (vowels.count(voweled)) tmp = vowels[voweled];
                }
            }
            res.push_back(tmp);
        }
        return res;
    }
    
    string toLowerStr(const string& s) {
        string res;
        for (const char& c : s) res += tolower(c);
        return res;
    }
    
    string toVowelStr(const string& s) {
        string res;
        for (char c : s) {
            const char t = tolower(c);
            if (vowels.count(t)) res += '*';
            else res += t;
        }
        return res;
    }
    
private:
    unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};
};