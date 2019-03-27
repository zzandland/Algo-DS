#ifndef BST_H
#define BST_H

#include <iostream>
#include <vector>

#include "Queue.h"

template <class T>
class BST {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;

    Node(T data);
  };

  class ListNode {
   public:
    T data_;
    ListNode *next_;

    ListNode(T data);
    void PrintList();
  };

  BST();
  virtual ~BST();
  void Insert(T data);
  bool Contains(T data);
  void Delete(T data);
  std::vector<ListNode *> ListOfDepths();

 private:
  Node *root_;

  Node *InsertHelper(Node *node, T data);
  bool ContainsHelper(Node *node, T data);
  Node *DeleteHelper(Node *node, T data);
};

template <class T>
BST<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BST<T>::ListNode::ListNode(T data) {
  data_ = data;
  next_ = nullptr;
}

template <class T>
void BST<T>::ListNode::PrintList() {
  ListNode* it = this;
  while (it != nullptr) {
    std::cout << it->data_ << "  ";
    it = it->next_;
  }
  std::cout << std::endl;
}

template <class T>
BST<T>::BST() {
  root_ = nullptr;
}

template <class T>
BST<T>::~BST() {
  while (root_ != nullptr) Delete(root_->data_);

  delete root_;
  delete this;
}

template <class T>
void BST<T>::Insert(T data) {
  Node *n = new Node(data);
  if (root_ == nullptr)
    root_ = n;
  else
    InsertHelper(root_, data);
}

template <class T>
bool BST<T>::Contains(T data) {
  return ContainsHelper(root_, data);
}

template <class T>
void BST<T>::Delete(T data) {
  DeleteHelper(root_, data);
}

template <class T>
std::vector<typename BST<T>::ListNode *> BST<T>::ListOfDepths() {
  std::vector<BST<T>::ListNode *> output;
  Queue<Node*> *q = new Queue<Node*>();
  q->Enqueue(root_);

  while (!q->Empty()) {
    int size = q->Size();
    ListNode *head = nullptr, *it = nullptr;
    for (int i = 0; i < size; ++i) {
      Node *n = q->Top();
      q->Dequeue();
      ListNode* ln = new ListNode(n->data_);
      if (it != nullptr) it->next_ = ln;
      it = ln;
      if (head == nullptr) head = it;
      if (n->left_ != nullptr) q->Enqueue(n->left_);
      if (n->right_ != nullptr) q->Enqueue(n->right_);
    }
    output.push_back(head);
  }
  return output;
}

template <class T>
typename BST<T>::Node *BST<T>::InsertHelper(Node *node, T data) {
  if (node == nullptr) return new Node(data);

  if (node->data_ > data)
    node->left_ = InsertHelper(node->left_, data);
  else
    node->right_ = InsertHelper(node->right_, data);
  return node;
}

template <class T>
bool BST<T>::ContainsHelper(Node *node, T data) {
  if (node == nullptr) return false;

  if (node->data_ == data)
    return true;
  else if (node->data_ > data)
    return ContainsHelper(node->left_, data);
  else
    return ContainsHelper(node->right_, data);
}

template <class T>
typename BST<T>::Node *BST<T>::DeleteHelper(Node *node, T data) {
  if (node == nullptr) return nullptr;

  if (node->data_ == data) {
    Node *temp = node;
    if (node->left_ == nullptr) {
      node = DeleteHelper(node->right_, data);
      delete temp;
    } else if (node->right_ == nullptr) {
      node = DeleteHelper(node->left_, data);
      delete temp;
    } else {
      Node *temp = node->right_;
      while (temp->left_ != nullptr) temp = temp->left_;
      node->data_ = temp->data_;
      DeleteHelper(node->right_, node->data_);
      delete temp;
    }
  } else if (node->data_ > data) {
    node->left_ = DeleteHelper(node->left_, data);
  } else {
    node->right_ = DeleteHelper(node->right_, data);
  }
  return node;
}

#endif /* BST_H */
