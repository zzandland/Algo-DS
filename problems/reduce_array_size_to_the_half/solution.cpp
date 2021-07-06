class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> freq;
        for (int n : arr) ++freq[n];
        int total, cur, res;
        total = cur = res = 0;
        priority_queue<int, vector<int>> pq;
        for (auto [_, cnt] : freq) {
            total += cnt;
            pq.push(cnt);
        }
        while (cur < total / 2) {
            ++res;
            cur += pq.top();
            pq.pop();
        }
        return res;
    }
};