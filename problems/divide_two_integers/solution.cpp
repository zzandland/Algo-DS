class Solution {
public:
    long signChange(int n, bool &sign) {
        long res = n;
        if (n < 0) {
            sign = !sign;
            return res * -1;
        }
        return res;
    }
    
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        bool sign = true;
        long a = signChange(dividend, sign);
        long b = signChange(divisor, sign);
        stack<pair<long, long>> st;
        st.push({b, 1});
        long res = 0;
        
        while (a >= b) {
            auto [n, c] = st.top();
            a -= n;
            res += c;
            if (a < b) break;
            if (a >= n + n) {
                st.push({n + n, c + c});
            } else {
                while (st.top().first > a) st.pop();
            }
        }
        return sign ? res : res * -1;
    }
};