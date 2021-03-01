class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> seen;
        for (const int &type : candyType) {
            if (!seen.count(type)) seen.emplace(type);
        }
        return min(candyType.size() / 2, seen.size());
    }
};