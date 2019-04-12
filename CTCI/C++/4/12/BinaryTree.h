#ifndef BINARYTREE_H
#define BINARYTREE_H

#include <iostream>
#include <map>

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
  int PathSum(T target);

 private:
  int PathSumHelper(Node* node, const T target, T running_sum,
                    std::map<T, int>& sum_map);
  void ManageMap(std::map<T, int>& sum_map, T key, int value);
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
int BinaryTree<T>::PathSum(T target) {
  std::map<T, int> sum_map;
  return PathSumHelper(root_, target, 0, sum_map);
}

template <class T>
int BinaryTree<T>::PathSumHelper(Node* node, const T target, T running_sum,
                                 std::map<T, int>& sum_map) {
  if (node == nullptr) return 0;
  int count = 0;
  running_sum += node->data_;
  ManageMap(sum_map, running_sum, 1);
  T offset = running_sum - target;
  if (sum_map.find(offset) != sum_map.end()) count += sum_map[offset];
  count += PathSumHelper(node->left_, target, running_sum, sum_map);
  count += PathSumHelper(node->right_, target, running_sum, sum_map);
  ManageMap(sum_map, running_sum, -1);
  return count;
}

template <class T>
void BinaryTree<T>::ManageMap(std::map<T, int>& sum_map, T key, int value) {
  if (sum_map.find(key) == sum_map.end()) sum_map.insert({key, 0});
  sum_map[key] += value;
  if (sum_map[key] <= 0) sum_map.erase(key);
}

#endif /* BINARYTREE_H */
