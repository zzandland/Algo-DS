class Solution {
public:
    int findTheWinner(int n, int k) {
        int cur = 0;
        vector<int> seat(n, true);
        for (int i = 0; i < n - 1; ++i) {
            int mv = k;
            while (mv > 0) {
                if (seat[cur]) --mv;
                cur = (cur + 1) % n;
            }
            seat[(cur + n - 1) % n] = false;
        }
        for (int i = 0; i < n; ++i) if (seat[i]) return i+1;
        return 0;
    }
};