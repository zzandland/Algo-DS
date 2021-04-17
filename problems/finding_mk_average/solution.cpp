class MKAverage {
public:
    int m, k, sum;
    queue<int> q;
    multiset<int> left, mid, right;
    MKAverage(int m, int k) : m(m), k(k), sum(0) {}
    
    void print() {
        for (auto n : left) cout << n << ':';
        cout << endl;
        for (auto n : mid) cout << n << ':';
        cout << endl;
        for (auto n : right) cout << n << ':';
        cout << "\n\n";
    }
    
    void addElement(int num) {
        q.push(num);
        left.insert(num);
        if (q.size() > m) {
            remove(q.front());
            q.pop();
        }
    }
    
    void remove(int num) {
        if (left.count(num)) {
            left.erase(left.find(num));
        } else if (mid.count(num)) {
            mid.erase(mid.find(num));
            sum -= num;
        } else { 
            right.erase(right.find(num));
        }
    }
    
    void rebalance() {
        int tmp;
        while (left.size() > k) {
            tmp = *left.rbegin();
            sum += tmp;
            left.erase(left.find(tmp));
            mid.insert(tmp);
        }
        while (right.size() < k) {
            tmp = *mid.rbegin();
            sum -= tmp;
            mid.erase(mid.find(tmp));
            right.insert(tmp);
        }
        while (*left.rbegin() > *mid.begin()) {
            int l = *left.rbegin(), m = *mid.begin();
            sum += l - m;
            mid.insert(l);
            left.insert(m);
            mid.erase(mid.find(m));
            left.erase(left.find(l));
        }
        while (*mid.rbegin() > *right.begin()) {
            int m = *mid.rbegin(), r = *right.begin();
            sum += r - m;
            mid.insert(r);
            right.insert(m);
            mid.erase(mid.find(m));
            right.erase(right.find(r));
        }
    }
    
    int calculateMKAverage() {
        if (q.size() < m) return -1;
        rebalance();
        return sum / (m - k - k);
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */