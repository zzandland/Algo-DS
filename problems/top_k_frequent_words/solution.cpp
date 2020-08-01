typedef pair<int, string> p;

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for (string word: words) freq[word] += 1;
        
        auto compare = [](p& a, p& b) {
            return a.first == b.first ? a.second.compare(b.second) < 0 : a.first > b.first;
        };
        
        priority_queue<p, vector<p>, decltype(compare)> pq(compare);
        
        for (auto it = freq.begin(); it != freq.end(); ++it) {
            p i(it->second, it->first);
            pq.emplace(i);
            if (pq.size() > k) pq.pop();
        }
        
        vector<string> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        
        reverse(res.begin(), res.end());
        return res;
    }
};