class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        // [[100,200],[1000,1250],[200,1300],[2000,3200]]
        // 0 100 1100 1300
        auto cmp = [&](const auto &a, const auto &b) {
            return a[1] == b[1] ? a[0] < b[0] : a[1] < b[1];
        };
        sort(courses.begin(), courses.end(), cmp);
        priority_queue<int, vector<int>> pq;
        int total = 0;
        for (auto c : courses) {
            if (total + c[0] <= c[1]) {
                total += c[0];
                pq.push(c[0]);
            } else if (!pq.empty() && pq.top() > c[0]) {
                total -= pq.top();
                pq.pop();
                total += c[0];
                pq.push(c[0]);
            }
        }
        return pq.size();
    }
};