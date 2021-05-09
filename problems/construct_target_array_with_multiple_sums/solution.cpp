class Solution {
public:
    bool isPossible(vector<int>& target) {
        if (target.size() == 1) return target[0] == 1;
        priority_queue<int, vector<int>> pq;
        long sum = 0;
        for (int n : target) {
            pq.push(n);
            sum += n;
        }
        while (pq.top() > 1) {
            int mx = pq.top();
            pq.pop();
            sum -= mx;
            if (mx <= sum) return false;
            int rem = mx % sum;
            if (rem == 0) return pq.top() == 1;
            pq.push(rem);
            sum += rem;
        }
        return true;
    }
};