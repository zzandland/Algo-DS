#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>

template <class T>
class Queue {
 public:
  Queue();
  virtual ~Queue();
  void Enqueue(T data);
  void Dequeue();
  T Top();
  bool Empty();
  int Size();

 private:
  class Node {
   public:
    T data_;
    Node *next_;

    Node(T data);
  };

  Node *head_, *tail_;
  int size_;
};

template <class T>
Queue<T>::Node::Node(T data) {
  data_ = data;
  next_ = nullptr;
}

template <class T>
Queue<T>::Queue() {
  head_ = tail_ = nullptr;
  size_ = 0;
}

template <class T>
Queue<T>::~Queue() {
  while (!Empty()) Dequeue();
  delete this;
}

template <class T>
void Queue<T>::Enqueue(T data) {
  size_++;
  Node *n = new Node(data);
  if (tail_ != nullptr) tail_->next_ = n;
  tail_ = n;
  if (head_ == nullptr) head_ = tail_;
}

template <class T>
void Queue<T>::Dequeue() {
  if (Empty()) {
    std::cout << "The queue is empty. Cannot dequeue." << std::endl;
    return;
  } 
  size_--;
  Node *temp = head_;
  head_ = head_->next_;
  delete temp;
  if (head_ == nullptr) tail_ = nullptr;
}

template <class T>
T Queue<T>::Top() {
  return head_->data_;
}

template <class T>
bool Queue<T>::Empty() {
  return head_ == nullptr;
}

template <class T>
int Queue<T>::Size() {
  return size_;
}

#endif /* QUEUE_H */
