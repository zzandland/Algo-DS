#ifndef BST_H
#define BST_H

#include <iostream>
#include <vector>

template <class T>
class BST {
 public:
  BST();
  BST(std::vector<T> arr);
  // virtual ~BST();
  void Insert(T data);
  int GetMaxHeight();

 private:
  class Node {
   public:
    T data_;
    Node *left_, *right_;

    Node(T data);
  };
  Node* root_ = nullptr;
  Node* InsertHelper(Node* n, T data);
  void GetHeightHelper(Node* n, int curr, int& max);
  Node* MakeMinTree(std::vector<T> arr, int left, int right);
};

template <class T>
BST<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BST<T>::BST() {
  root_ = nullptr;
}

template <class T>
BST<T>::BST(std::vector<T> arr) {
  root_ = MakeMinTree(arr, 0, arr.size() - 1);
}

template <class T>
void BST<T>::Insert(T data) {
  if (root_ == nullptr)
    root_ = new Node(data);
  else {
    InsertHelper(root_, data);
  }
}

template <class T>
typename BST<T>::Node* BST<T>::InsertHelper(Node* n, T data) {
  if (n == nullptr) return new Node(data);
  if (data < n->data_)
    n->left_ = InsertHelper(n->left_, data);
  else
    n->right_ = InsertHelper(n->right_, data);
  return n;
}

template <class T>
int BST<T>::GetMaxHeight() {
  int max = 0;
  GetHeightHelper(root_, 0, max);
  return max;
}

template <class T>
void BST<T>::GetHeightHelper(Node* n, int curr, int& max) {
  if (n == nullptr) {
    if (curr > max) max = curr;
    return;
  }  
  GetHeightHelper(n->left_, curr + 1, max);
  GetHeightHelper(n->right_, curr + 1, max);
}

template <class T>
typename BST<T>::Node* BST<T>::MakeMinTree(std::vector<T> arr, int left, int right) {
  if (left > right) {
    return NULL;
  }
  int mid = left + (right - left) / 2;
  Node* n = new Node(arr[mid]);
  n->left_ = MakeMinTree(arr, left, mid - 1);
  n->right_ = MakeMinTree(arr, mid + 1, right);
  return n;
}

#endif /* BST_H */
