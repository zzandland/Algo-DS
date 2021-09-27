class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> uniq_emails;
        stringstream ss;
        for (const string & email : emails) {
            string s;
            for (const char c : email) {
                if (c == '+' || c == '@') break;
                if (c == '.') continue;
                s += c;
            }
            s += email.substr(email.find('@'));
            uniq_emails.insert(s);
        }
        return uniq_emails.size();
    }
};