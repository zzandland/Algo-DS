class MyCalendarThree {
public:
    map<int, int> delta;
    
    MyCalendarThree() {}
    
    int book(int start, int end) {
        delta[start] += 1;
        delta[end] -= 1;
        
        int curr = 0, mx = 0;
        for (auto it = delta.begin(); it != delta.end(); ++it) {
            curr += it->second;
            mx = max(mx, curr);
        }
        return mx;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */