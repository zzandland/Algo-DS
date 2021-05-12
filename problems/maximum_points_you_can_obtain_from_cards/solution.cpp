class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int sum, run, mn = INT_MAX, len = cardPoints.size();
        sum = run = 0;
        for (int i = 0, j = 0; i < len; ++i) {
            run += cardPoints[i];
            sum += cardPoints[i];
            if (i >= len - k) run -= cardPoints[j++];  
            if (i >= len - k - 1) mn = min(mn, run);
        }
        return sum - mn;
    }
};