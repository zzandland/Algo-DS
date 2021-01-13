class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int l, r, res, tmp;
        l = res = 0;
        r = people.size() - 1;
        while (l <= r) {
            res++;
            tmp = people[r--];
            if (l <= r && tmp + people[l] <= limit) {
                tmp += people[l++];
            }
        }
        return res;
    }
};