class MedianFinder {
public:
    priority_queue<int, vector<int>> l;
    priority_queue<int, vector<int>, greater<int>> r;
    /** initialize your data structure here. */
    MedianFinder() {}
    
    void addNum(int num) {
        l.push(num);
        r.push(l.top());
        l.pop();
        l.push(r.top());
        r.pop();
        if (l.size() > r.size() + 1) {
            r.push(l.top());
            l.pop();
        }
    }
    
    double findMedian() {
        if (l.size() > r.size()) return l.top();
        return (l.top() + r.top()) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */