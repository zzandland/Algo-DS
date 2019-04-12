#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include <iostream>

template <class T>
class BinaryTree {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;

    Node(T data);
    virtual ~Node();
  };

  Node* root_;

  BinaryTree();
  virtual ~BinaryTree();
  bool CheckSubtreeRuntime(BinaryTree* bst);
  bool CheckSubtreeMemory(BinaryTree* bst);

 private:
  bool RuntimeHelper(Node* large, Node* small);
  void PreOrderString(Node* node, std::string& str);
  bool MemoryHelper(Node* large, Node* small);
  bool Compare(Node* large, Node* small);
};

template <class T>
BinaryTree<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BinaryTree<T>::Node::~Node() {
  delete left_;
  delete right_;
}

template <class T>
BinaryTree<T>::BinaryTree() {
  root_ = nullptr;
}

template <class T>
BinaryTree<T>::~BinaryTree() {
  delete root_;
}

template <class T>
bool BinaryTree<T>::CheckSubtreeRuntime(BinaryTree* bst) {
  if (bst->root_ == nullptr)
    return true;
  else if (root_ == nullptr)
    return false;
  return RuntimeHelper(this->root_, bst->root_);
}

template <class T>
bool BinaryTree<T>::RuntimeHelper(Node* large, Node* small) {
  std::string large_seq;
  std::string small_seq;
  PreOrderString(large, large_seq);
  PreOrderString(small, small_seq);
  std::cout << large_seq << "//" << small_seq << std::endl;
  return large_seq.find(small_seq) != std::string::npos;
}

template <class T>
void BinaryTree<T>::PreOrderString(Node* node, std::string& str) {
  if (node == nullptr) return;
  str += std::to_string(node->data_);
  PreOrderString(node->left_, str);
  PreOrderString(node->right_, str);
}

template <class T>
bool BinaryTree<T>::CheckSubtreeMemory(BinaryTree* bst) {
  if (bst->root_ == nullptr)
    return true;
  else if (root_ == nullptr)
    return false;
  return MemoryHelper(this->root_, bst->root_);
}

template <class T>
bool BinaryTree<T>::MemoryHelper(Node* large, Node* small) {
  if (large == nullptr) return false;
    std::cout << large->data_ << " " << small->data_ << std::endl;
  if (large->data_ == small->data_ && Compare(large, small)) return true;

  return MemoryHelper(large->left_, small) ||
         MemoryHelper(large->right_, small);
}

template <class T>
bool BinaryTree<T>::Compare(Node* large, Node* small) {
  if (large == nullptr && small == nullptr) {
    return true;
  } else if (large == nullptr || small == nullptr) {
    return false;
  } else if (large->data_ != small->data_) {
    return false;
  } else {
    return Compare(large->left_, small->left_) &&
           Compare(large->right_, small->right_);
  }
}

#endif /* BINARY_TREE_H */
