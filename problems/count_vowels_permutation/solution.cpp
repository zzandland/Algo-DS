class Solution {
public:
    unordered_map<char, vector<char>> mp{
        {'a', {'e'}},
        {'e', {'a', 'i'}},
        {'i', {'a', 'e', 'o', 'u'}},
        {'o', {'i', 'u'}},
        {'u', {'a'}}
    };
    
    int countVowelPermutation(int n) {
        long a, e, i, o, u, na, ne, ni, no, nu;
        int MOD = (int)(pow(10, 9) + 7);
        a = e = i = o = u = 1;
        for (int j = 1; j < n; ++j) {
            na = e % MOD;
            ne = (a + i) % MOD;
            ni = (a + e + o + u) % MOD;
            no = (i + u) % MOD;
            nu = a % MOD;
            a = na;
            e = ne;
            i = ni;
            o = no;
            u = nu;
        }
        return (a + e + i + o + u) % MOD;
    }
};