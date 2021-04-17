class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        int arr[] = {INT_MAX, 0, INT_MAX};
        int prev = 1;
        for (int n : obstacles) {
            if (n != 0) {
                arr[n-1] = INT_MAX;
                prev = 0;
                for (int i = 0; i < 3; ++i) {
                    if (arr[prev] > arr[i]) prev = i;
                }
            }
            for (int i = 0; i < 3; ++i) {
                if (prev != i && i != n-1) arr[i] = min(arr[i], arr[prev] + 1);
            }
        }
        return min(arr[0], min(arr[1], arr[2]));
    }
};