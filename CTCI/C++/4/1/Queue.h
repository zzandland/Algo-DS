#ifndef QUEUE_H
#define QUEUE_H

#include "Error.h"

template <class Y>
class Queue {
 public:
  class Node {
   private:
    Y data_;
    Node* next_;

   public:
    Node(Y data);

    Y GetData();

    Node* GetNext();

    void SetNext(Node* node);
  };

  Queue();

  ~Queue();

  void Enqueue(Y data);

  void Dequeue();

  Y Top();

  bool Empty();

 private:
  Node* head_;
  Node* tail_;
};

template <class Y>
Queue<Y>::Node::Node(Y data) {
  data_ = data;
  next_ = nullptr;
}

template <class Y>
Y Queue<Y>::Node::GetData() {
  return data_;
}

template <class Y>
typename Queue<Y>::Node* Queue<Y>::Node::GetNext() {
  return next_;
}

template <class Y>
void Queue<Y>::Node::SetNext(Node* node) {
  next_ = node;
}

template <class Y>
Queue<Y>::Queue() {
  head_ = nullptr;
  tail_ = nullptr;
}

template <class Y>
Queue<Y>::~Queue() {
  while (head_->next_ != nullptr) {
    Node* prev = head_;
    head_ = head_->next_;
    delete prev;
  }
  delete head_;
  delete tail_;
  delete this;
}

template <class Y>
void Queue<Y>::Enqueue(Y data) {
  Node* item = new Node(data);
  if (head_ != nullptr)
    tail_->SetNext(item);
  else
    head_ = item;
  tail_ = item;
}

template <class Y>
void Queue<Y>::Dequeue() {
  if (Empty()) {
    throw new Error("***Queue is empty***");
  }
  head_ = head_->GetNext();
  if (head_ == nullptr) tail_ = nullptr;
}

template <class Y>
Y Queue<Y>::Top() {
  return head_->GetData();
}

template <class Y>
bool Queue<Y>::Empty() {
  return head_ == nullptr;
}

#endif /* QUEUE_H */
