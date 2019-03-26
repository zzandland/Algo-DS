class MinStack {
public:
  /** initialize your data structure here. */
  MinStack() {
    stack_top_ = nullptr;
    min_top_ = nullptr;
  }

  void push(int x) {
    Node *n = new Node(x);
    Node *min_node = nullptr;
    if (!empty()) {
      n->next_ = stack_top_;
      int min_data = min_top_->data_;
      if (min_data > x) min_node = new Node(x);
      else min_node = new Node(min_data);  
      min_node->next_ = min_top_;
    }
    stack_top_ = n;
    if (min_node == nullptr) min_top_ = new Node(x);
    else min_top_ = min_node;
  }

  void pop() {
    stack_top_ = stack_top_->next_;
    min_top_ = min_top_->next_;
  }

  int top() {
    return stack_top_->data_;
  }

  int getMin() {
    return min_top_->data_;
  }
  
  bool empty() {
    return stack_top_ == nullptr;
  }
  
private:
  class Node {
  public:
    int data_;
    Node *next_;

    Node(int data) {
      data_ = data;
      next_ = nullptr;
    }
  };
  
  Node* stack_top_;
  Node* min_top_;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */