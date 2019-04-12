#ifndef BST_H
#define BST_H

#include <iostream>
#include <list>
#include <vector>

template <class T>
class BST {
 public:
  class Node {
   public:
    T data_;
    Node *left_, *right_;
    Node(T data);
    ~Node();
  };

  typedef int (*comparatorFcn)(T val1, T val2);

  BST(T data, comparatorFcn cmpr);
  virtual ~BST();
  void InsertNode(T data);
  void DeleteNode(T data);
  Node* Find(T data) const;
  bool ValidateBST();
  std::vector<std::vector<T>> Sequences();
  std::vector<std::list<T>> Sequences2();

 private:
  Node* root_;
  comparatorFcn cmpr_;
  Node* InsertNodeHelper(Node* node, T data);
  Node* DeleteNodeHelper(Node* node, T data);
  Node* FindHelper(Node* node, T data) const;
  bool ValidateBSTHelper(Node* node, T* low, T* high);
  void SequencesHelper(std::vector<Node*> pool, std::vector<T>& arr,
                       std::vector<std::vector<T>>& output);
  void Swapper(Node* target, std::vector<Node*> pool, std::vector<T>& arr,
               std::vector<std::vector<T>>& output);
  std::vector<std::list<T>> Sequences2Helper(Node* node);
  void Weave(std::list<T>& left, std::list<T>& right, std::list<T>& preset, std::vector<std::list<T>>& output);
};

template <class T>
using NodePtr = typename BST<T>::Node*;

template <class T>
BST<T>::Node::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
BST<T>::Node::~Node() {
  delete left_;
  delete right_;
}

template <class T>
BST<T>::BST(T data, comparatorFcn cmpr) {
  root_ = new Node(data);
  cmpr_ = cmpr;
}

template <class T>
BST<T>::~BST() {
  delete root_;
}

template <class T>
void BST<T>::InsertNode(T data) {
  InsertNodeHelper(root_, data);
}

template <class T>
NodePtr<T> BST<T>::InsertNodeHelper(Node* node, T data) {
  if (node == nullptr) return new Node(data);

  if (cmpr_(node->data_, data) < 0)
    node->left_ = InsertNodeHelper(node->left_, data);
  else
    node->right_ = InsertNodeHelper(node->right_, data);
  return node;
}

template <class T>
void BST<T>::DeleteNode(T data) {
  DeleteNodeHelper(root_, data);
}

template <class T>
NodePtr<T> BST<T>::DeleteNodeHelper(Node* node, T data) {
  if (node == nullptr) return node;

  if (node->data_ == data) {
    if (node->left_ == nullptr) return DeleteNodeHelper(node->right_, data);
    if (node->right_ == nullptr) return DeleteNodeHelper(node->left_, data);
    Node* temp = node->right_;
    while (temp->left_ != nullptr) temp = temp->left_;
    node->data_ = temp->data_;
    temp = nullptr;
    DeleteNodeHelper(node->right_, node->data_);
  }

  if (cmpr_(node->data_, data) < 0)
    node->left_ = DeleteNodeHelper(node->left_, data);
  else
    node->right_ = DeleteNodeHelper(node->right_, data);
  return node;
}

template <class T>
NodePtr<T> BST<T>::Find(T data) const {
  return FindHelper(root_, data);
}

template <class T>
NodePtr<T> BST<T>::FindHelper(Node* node, T data) const {
  if (node == nullptr) return node;
  if (node->data_ == data) return node;
  if (cmpr_(node->data_, data) < 0)
    return FindHelper(node->left_, data);
  else
    return FindHelper(node->right_, data);
}

template <class T>
bool BST<T>::ValidateBST() {
  return ValidateBSTHelper(root_, nullptr, nullptr);
}

template <class T>
bool BST<T>::ValidateBSTHelper(Node* node, T* low, T* high) {
  if (node == nullptr) return true;

  T data = node->data_;

  if (low != nullptr && cmpr_(data, *low) > 0) return false;
  if (high != nullptr && cmpr_(data, *high) < 0) return false;

  if (node->left_ != nullptr && cmpr_(data, node->left_->data_) >= 0)
    return false;
  if (node->right_ != nullptr && cmpr_(data, node->right_->data_) < 0)
    return false;

  return ValidateBSTHelper(node->left_, low, &data) &&
         ValidateBSTHelper(node->right_, &data, high);
}

template <class T>
std::vector<std::vector<T>> BST<T>::Sequences() {
  std::vector<std::vector<T>> output;
  std::vector<T> arr;
  std::vector<Node*> pool = {root_};
  SequencesHelper(pool, arr, output);
  return output;
}

template <class T>
void BST<T>::SequencesHelper(std::vector<Node*> pool, std::vector<T>& arr,
                             std::vector<std::vector<T>>& output) {
  if (pool.empty()) {
    std::vector<T> temp(arr);
    output.push_back(temp);
    return;
  }

  for (size_t i = 0; i < pool.size(); ++i) Swapper(pool[i], pool, arr, output);
}

template <class T>
void BST<T>::Swapper(Node* target, std::vector<Node*> pool, std::vector<T>& arr,
                     std::vector<std::vector<T>>& output) {
  for (size_t i = 0; i < pool.size(); ++i) {
    if (pool[i] == target) {
      arr.push_back(target->data_);
      pool.erase(pool.begin() + i);
      if (target->left_ != nullptr) pool.push_back(target->left_);
      if (target->right_ != nullptr) pool.push_back(target->right_);
      SequencesHelper(pool, arr, output);
      arr.pop_back();
    }
  }
}

template <class T>
std::vector<std::list<T>> BST<T>::Sequences2() {
  return Sequences2Helper(root_);
}

template <class T>
std::vector<std::list<T>> BST<T>::Sequences2Helper(Node* node) {
  std::vector<std::list<T>> output;
  if (node == nullptr) {
    output.push_back(std::list<T>());
    return output;
  }
  std::vector<std::list<T>> left_seqs = Sequences2Helper(node->left_);
  std::vector<std::list<T>> right_seqs = Sequences2Helper(node->right_);
  std::list<T> preset = {node->data_};
  for (std::list<T> left_seq : left_seqs)
    for (std::list<T> right_seq : right_seqs)
      Weave(left_seq, right_seq, preset, output);
  return output;
}

template <class T>
void BST<T>::Weave(std::list<T>& left, std::list<T>& right, std::list<T>& preset, std::vector<std::list<T>>& output) {
  if (left.size() == 0 || right.size() == 0) {
    std::list<T> temp = {preset};
    temp.insert(temp.end(), left.begin(), left.end());
    temp.insert(temp.end(), right.begin(), right.end());
    output.push_back(temp);
    return;
  }

  T left_head = left.front();
  left.pop_front();
  preset.push_back(left_head);
  Weave(left, right, preset, output);
  preset.pop_back();
  left.push_front(left_head);

  T right_head = right.front();
  right.pop_front();
  preset.push_back(right_head);
  Weave(left, right, preset, output);
  preset.pop_back();
  right.push_front(right_head);
}

#endif /* BST_H */
