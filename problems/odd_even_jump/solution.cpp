class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int N = A.size();
        map<int, int> seen;
        vector<int> odds(N), evens(N);
        odds[N-1] = evens[N-1] = 1;
        int res = 1;
        seen[A[N-1]] = N-1;
        
        for (int i = N-2; i >= 0; --i) {
            auto odd = seen.lower_bound(A[i]), even = seen.upper_bound(A[i]);
            if (odd != seen.end()) odds[i] = evens[odd->second];
            if (even != seen.begin()) evens[i] = odds[(--even)->second];  
            if (odds[i]) ++res;
            seen[A[i]] = i;
        }
        
        return res;
    }
};