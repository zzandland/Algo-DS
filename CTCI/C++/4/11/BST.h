#ifndef BST_H
#define BST_H

#include <iostream>
#include <random>

template <class T>
class BST {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;
    int nLeft, nRight;
    Node(T data);
    ~Node();
  };
  BST();
  virtual ~BST();
  void Insert(T data);
  void Delete(T data);
  Node* Find(T data);
  Node* RandomNode();
  void Iterate();

 private:
  Node* root_;
  Node* InsertHelper(Node* root, T data);
  Node* DeleteHelper(Node* root, T data);
  Node* FindHelper(Node* root, T data);
  Node* RandomNodeHelper(Node* root, std::mt19937& rng);
  void IterateHelper(Node* root);
};

template <class T>
using Nodeptr = typename BST<T>::Node*;

template <class T>
BST<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
  nLeft = nRight = 0;
}

template <class T>
BST<T>::Node::~Node() {
  delete left_;
  delete right_;
}

template <class T>
BST<T>::BST() {
  root_ = nullptr;
}

template <class T>
BST<T>::~BST() {
  delete root_;
}

template <class T>
void BST<T>::Insert(T data) {
  if (root_ == nullptr)
    root_ = new Node(data);
  else
    InsertHelper(root_, data);
}

template <class T>
Nodeptr<T> BST<T>::InsertHelper(Node* root, T data) {
  if (root == nullptr) return new Node(data);
  if (root->data_ > data) {
    root->nLeft++;
    root->left_ = InsertHelper(root->left_, data);
  } else {
    root->nRight++;
    root->right_ = InsertHelper(root->right_, data);
  }
  return root;
}

template <class T>
void BST<T>::Delete(T data) {
  DeleteHelper(root_, data);
}

template <class T>
Nodeptr<T> BST<T>::DeleteHelper(Node* root, T data) {
  if (root == nullptr) return root;
  if (root->data_ == data) {
    if (root->left_ == nullptr) {
      return root->right_;
    } else if (root->right_ == nullptr) {
      return root->left_;
    } else {
      Node* temp = root->right_;
      root->nRight--;
      while (temp->left_ != nullptr) temp = temp->left_;
      root->data_ = temp->data_;
      root->right_ = DeleteHelper(root->right_, root->data_);
      return root;
    }
  }
  if (root->data_ > data) {
    root->nLeft--;
    root->left_ = DeleteHelper(root->left_, data);
  } else {
    root->nRight--;
    root->right_ = DeleteHelper(root->right_, data);
  }
  return root;
}

template <class T>
Nodeptr<T> BST<T>::Find(T data) {
  return FindHelper(root_, data);
}

template <class T>
Nodeptr<T> BST<T>::FindHelper(Node* root, T data) {
  if (root->data_ == data)
    return root;
  else if (root->data_ > data)
    return FindHelper(root->left_, data);
  else
    return FindHelper(root->right_, data);
}

template <class T>
void BST<T>::Iterate() {
  IterateHelper(root_);
}

template <class T>
void BST<T>::IterateHelper(Node* root) {
  if (root == nullptr) return;
  std::cout << "Val: " << root->data_ << ", left: " << root->nLeft
            << ", right: " << root->nRight << std::endl;
  IterateHelper(root->left_);
  IterateHelper(root->right_);
}

template <class T>
Nodeptr<T> BST<T>::RandomNode() {
  std::random_device dev;
  std::mt19937 rng(dev());
  return RandomNodeHelper(root_, rng);
}

template <class T>
Nodeptr<T> BST<T>::RandomNodeHelper(Node* root, std::mt19937& rng) {
  if (root->left_ == nullptr && root->right_ == nullptr) return root;
  std::uniform_int_distribution<int> ran_num(0, (1 + root->nLeft + root->nRight));
  int num = ran_num(rng);
  if (num == 0) 
    return root;
  else if (num <= root->nLeft)
    return RandomNodeHelper(root->left_, rng);
  else
    return RandomNodeHelper(root->right_, rng);
}

#endif /* BST_H */
