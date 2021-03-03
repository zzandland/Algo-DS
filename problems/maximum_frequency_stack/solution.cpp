class FreqStack {
public:
    unordered_map<int, int> num2freq;    
    unordered_map<int, stack<int>> freq2st;
    int mx = 0;

    FreqStack() {}
    
    void push(int x) {
        num2freq[x]++;
        freq2st[num2freq[x]].push(x);
        mx = max(mx, num2freq[x]);
    }
    
    int pop() {
        int res = freq2st[mx].top();
        freq2st[mx].pop();
        num2freq[res]--;
        if (freq2st[mx].empty()) mx--;
        return res;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */