struct Node {
    int n, f, t;
    
    Node(int n, int f, int t): n(n), f(f), t(t) {}
};

class Compare {
public:
    bool operator() (const Node *a, const Node *b) {
        if (a->f == b->f) return a->t < b->t;
        return a->f < b->f;
    }    
};


class FreqStack {
public:
    priority_queue<Node*, vector<Node*>, Compare> pq;
    unordered_map<int, int> dic;
    int t;
    
    FreqStack(): t(0) {}
    
    void push(int x) {
        dic[x]++;
        Node *tmp = new Node(x, dic[x], t++);
        pq.push(tmp);
    }
    
    int pop() {
        Node *tmp = pq.top();
        pq.pop();
        dic[tmp->n]--;
        return tmp->n;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */