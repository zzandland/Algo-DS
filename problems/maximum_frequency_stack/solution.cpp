class FreqStack {
public:
    unordered_map<int, stack<int>> m;
    unordered_map<int, int> freqs;
    int mx;
    
    FreqStack(): mx(0) {}
    
    void push(int x) {
        mx = max(mx, ++freqs[x]);
        m[freqs[x]].emplace(x);
    }
    
    int pop() {
        int x = m[mx].top();
        m[mx].pop();
        if (!m[mx].size()) mx -= 1;
        --freqs[x];
        return x;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */