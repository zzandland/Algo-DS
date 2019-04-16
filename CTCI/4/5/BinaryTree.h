#ifndef BINARYTREE_H
#define BINARYTREE_H

#include <iostream>

template <class T>
class BinaryTree {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;

    Node(T data);
  };

  Node *root_;

  BinaryTree();
  virtual ~BinaryTree();
  bool ValidateBST();
  void InsertBST(T data);
  void InOrderDFS(Node *node);

 private:
  void DeleteAll(Node *node);
  bool ValidateBSTHelper(Node *node, int *min, int *max);
  Node *InsertBSTHelper(Node *node, T data);
};

template <class T>
BinaryTree<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BinaryTree<T>::BinaryTree() {
  root_ = nullptr;
}

template <class T>
BinaryTree<T>::~BinaryTree() {
  DeleteAll(root_);
}

template <class T>
bool BinaryTree<T>::ValidateBST() {
  int *min = nullptr, *max = nullptr;
  return ValidateBSTHelper(root_, min, max);
}

template <class T>
void BinaryTree<T>::InsertBST(T data) {
  if (root_ == nullptr)
    root_ = new Node(data);
  else
    InsertBSTHelper(root_, data);
}

template <class T>
void BinaryTree<T>::InOrderDFS(Node *node) {
  if (node == nullptr) return;

  InOrderDFS(node->left_);
  std::cout << node->data_ << ":";
  InOrderDFS(node->right_);
}

template <class T>
void BinaryTree<T>::DeleteAll(Node *node) {
  if (node->left_) DeleteAll(node->left_);
  if (node->right_) DeleteAll(node->right_);
  delete node;
}

template <class T>
bool BinaryTree<T>::ValidateBSTHelper(Node *node, int *min, int *max) {
  if (node == nullptr) return true;
  if (min != nullptr && node->data_ < *min) return false;
  if (max != nullptr && node->data_ > *max) return false;
  return ValidateBSTHelper(node->left_, min, &node->data_) &&
         ValidateBSTHelper(node->right_, &node->data_, max);
}

template <class T>
typename BinaryTree<T>::Node *BinaryTree<T>::InsertBSTHelper(Node *node,
                                                             T data) {
  if (node == nullptr) return new Node(data);

  if (data < node->data_)
    node->left_ = InsertBSTHelper(node->left_, data);
  else
    node->right_ = InsertBSTHelper(node->right_, data);

  return node;
}

#endif /* BINARYTREE_H */
