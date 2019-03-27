#ifndef BINARYTREE_H
#define BINARYTREE_H

#include <iostream>
#include <set>

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
  bool CheckIfBalanced();

 private:
  void DeleteAll(Node *node);
  bool CheckIfBalancedHelper(Node *node, int curr, std::set<int> &numset);
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
bool BinaryTree<T>::CheckIfBalanced() {
  std::set<int> numset;
  return CheckIfBalancedHelper(root_, 0, numset);
}

template <class T>
void BinaryTree<T>::DeleteAll(Node *node) {
  if (node->left_ != nullptr) DeleteAll(node->left_);
  if (node->right_ != nullptr) DeleteAll(node->right_);
  delete node;
}

template <class T>
bool BinaryTree<T>::CheckIfBalancedHelper(Node *node, int curr,
                                          std::set<int> &numset) {
  if (node == nullptr) {
    numset.insert(curr);
    return (numset.size() > 2) ? false : true;
  }

  if (!CheckIfBalancedHelper(node->left_, curr + 1, numset)) return false;

  if (!CheckIfBalancedHelper(node->right_, curr + 1, numset)) return false;

  return true;
}

#endif /* BINARYTREE_H */
