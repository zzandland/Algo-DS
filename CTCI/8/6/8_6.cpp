#include <iostream>

class Stack {
 public:
  class Node {
   public:
    int data_;
    Node* next_;
    Node(int disk) : data_(disk){};
    virtual ~Node() { delete next_; };
  };

  virtual ~Stack() { delete top_; }

  void Push(int disk) {
    Node* n = new Node(disk);
    if (top_ != nullptr) n->next_ = top_;
    top_ = n;
  }

  void Pop() { top_ = top_->next_; }

  int Top() { return top_->data_; };

  bool Empty() { return top_ == nullptr; };

  void Print() {
    Node* n = top_;
    while (n != nullptr) {
      std::cout << n->data_ << " ";
      n = n->next_;
    }
    std::cout << std::endl;
  }

 private:
  Node* top_;
};

class TowersOfHanoi {
 public:
  TowersOfHanoi(int n)
      : t1_(new Stack()), t2_(new Stack()), t3_(new Stack()), n_disk_(n) {
    for (int i = n; i >= 1; --i) t1_->Push(i);
  }

  void Move(Stack* from, Stack* to) {
    to->Push(from->Top());
    from->Pop();
  }

  void Solve() { MoveDisks(1, t1_, t3_, t2_); }

  void MoveDisks(int n, Stack* from, Stack* to, Stack* mid) {
    if (n == n_disk_ - 1) {
      Move(from, mid);
      Move(from, to);
      Move(mid, to);
      return;
    }
    MoveDisks(n + 1, from, mid, to);
    Move(from, to);
    MoveDisks(n + 1, mid, to, from);
  }

  void Print() {
    std::cout << "t1: ";
    t1_->Print();
    std::cout << "t2: ";
    t2_->Print();
    std::cout << "t3: ";
    t3_->Print();
    std::cout << std::endl;
  }

 private:
  Stack* t1_;
  Stack* t2_;
  Stack* t3_;
  int n_disk_;
};

int main(void) {
  TowersOfHanoi* t = new TowersOfHanoi(10);
  t->Print();
  t->Solve();
  t->Print();
  delete t;
  return 0;
}
