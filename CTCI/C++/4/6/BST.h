#ifndef BST_H
#define BST_H

#include <iostream>
#include <vector>

template <class T>
class BST {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;

    Node(T data);
    virtual ~Node();
  };

  Node* root_;
  BST();
  virtual ~BST();
  void Insert(T data);
  void Delete(T data);
  Node* Successor(T data);
  Node* Predecessor(T data);

 private:
  Node* InsertHelper(Node* node, T data);
  Node* DeleteHelper(Node* node, T data);
  void DestructorHelper(Node* node);
};

template <class T>
BST<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BST<T>::Node::~Node() {
  left_ = right_ = nullptr;
  delete this;
}

template <class T>
BST<T>::BST() {
  root_ = nullptr;
}

template <class T>
BST<T>::~BST() {
  DestructorHelper(root_);
}

template <class T>
void BST<T>::Insert(T data) {
  if (root_ == nullptr)
    root_ = new Node(data);
  else
    InsertHelper(root_, data);
}

template <class T>
typename BST<T>::Node* BST<T>::InsertHelper(Node* node, T data) {
  if (node == nullptr) return new Node(data);

  if (node->data_ > data)
    node->left_ = InsertHelper(node->left_, data);
  else
    node->right_ = InsertHelper(node->right_, data);

  return node;
}

template <class T>
void BST<T>::Delete(T data) {
  DeleteHelper(root_, data);
}

template <class T>
typename BST<T>::Node* BST<T>::DeleteHelper(Node* node, T data) {
  if (node == nullptr) return nullptr;

  if (node->data_ == data) {
    if (node->left_ == nullptr) {
      node = DeleteHelper(node->right_, data);
    } else if (node->right_ == nullptr) {
      node = DeleteHelper(node->left_, data);
    } else {
      Node* temp = node->right_;
      while (temp->left_ != nullptr) temp = temp->left_;
      node->data_ = temp->data_;
      node->right_ = DeleteHelper(node->right_, node->data_);
    }
  } else if (node->data_ > data) {
    node->left_ = DeleteHelper(node->left_, data);
  } else {
    node->right_ = DeleteHelper(node->right_, data);
  }
  return node;
}

template <class T>
typename BST<T>::Node* BST<T>::Successor(T data) {
  Node* node = root_;
  Node* succ = nullptr;
  while (node != nullptr) {
    if (node->data_ > data) {
      succ = node;
      node = node->left_;
    } else {
      node = node->right_;
    }
  }
  return succ;
}

template <class T>
typename BST<T>::Node* BST<T>::Predecessor(T data) {
  Node* node = root_;
  Node* pred = nullptr;
  while (node != nullptr) {
    if (node->data_ < data) {
      pred = node;
      node = node->right_;
    } else {
      node = node->left_;
    }
  }
  return pred;
}

template <class T>
void BST<T>::DestructorHelper(Node* node) {
  if (node->left_ != nullptr) DestructorHelper(node->left_);
  if (node->right_ != nullptr) DestructorHelper(node->right_);
  delete node;
}

#endif /* BST_H */
