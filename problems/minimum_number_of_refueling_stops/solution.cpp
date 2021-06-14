class Solution {
public:
    int minRefuelStops(int target, int fuel, vector<vector<int>>& stations) {
        priority_queue<int> pq;
        int res = 0, len = stations.size();
        for (int i = 0; i <= len; ++i) {
            int x = i == len ? target : stations[i][0];
            while (fuel < x && !pq.empty()) {
                fuel += pq.top();
                pq.pop();
                ++res;
            }
            if (fuel < x) return -1;
            if (i < len) pq.push(stations[i][1]);
        }
        return fuel >= target ? res : -1;
    }
};