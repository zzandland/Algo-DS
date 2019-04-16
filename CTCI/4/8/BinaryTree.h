#ifndef NODE_H_
#define NODE_H_

#include <iostream>

template <class T>
class Node {
 public:
  T data_;
  Node *left_, *right_;

  Node(T data);
  ~Node();

  bool FirstCommonAncestor(Node* node, Node* node1, Node* node2,
                           Node*& common_anc);
  Node* CommonAncestor(Node* root, Node* node1, Node* node2);
  Node* CommonAncestorHelper(Node* node, Node* node1, Node* node2);
  bool Contains(Node* node, Node* target);
  Node* Optimized(Node* node, Node* node1, Node* node2);
};

template <class T>
Node<T>::Node(T data) {
  data_ = data;
  left_ = right_ = nullptr;
}

template <class T>
Node<T>::~Node() {
  delete left_;
  delete right_;
}

template <class T>
bool Node<T>::FirstCommonAncestor(Node* node, Node* node1, Node* node2,
                                  Node*& common_anc) {
  if (node == nullptr) return false;
  if (node == node1 || node == node2) {
    common_anc = node;
    return true;
  }

  bool left = FirstCommonAncestor(node->left_, node1, node2, common_anc);
  bool right = FirstCommonAncestor(node->right_, node1, node2, common_anc);

  if (left && right) {
    common_anc = node;
    return true;
  } else if (left || right) {
    return true;
  } else {
    return false;
  }
}

template <class T>
Node<T>* Node<T>::CommonAncestor(Node* root, Node* node1, Node* node2) {
  if (!Contains(root, node1) || !Contains(root, node2)) return nullptr;

  if (Contains(node1, node2))
    return node1;
  else if (Contains(node2, node1))
    return node2;

  // return CommonAncestorHelper(root, node1, node2);
  return Optimized(root, node1, node2);
}

template <class T>
Node<T>* Node<T>::CommonAncestorHelper(Node* node, Node* node1, Node* node2) {
  if (node == nullptr) return nullptr;

  if ((Contains(node->left_, node1) && Contains(node->right_, node2)) ||
      (Contains(node->right_, node1) && Contains(node->left_, node2)))
    return node;

  Node* left_child = CommonAncestorHelper(node->left_, node1, node2);
  if (left_child != nullptr) return left_child;

  Node* right_child = CommonAncestorHelper(node->right_, node1, node2);
  if (right_child != nullptr) return right_child;

  return nullptr;
}

template <class T>
bool Node<T>::Contains(Node* node, Node* target) {
  if (node == nullptr)
    return false;
  else if (node == target)
    return true;
  return Contains(node->left_, target) || Contains(node->right_, target);
}

template <class T>
Node<T>* Node<T>::Optimized(Node* node, Node* node1, Node* node2) {
  if (node == nullptr || node == node1 || node == node2) return node;

  Node* left_tree = Optimized(node->left_, node1, node2);
  if (left_tree != nullptr && left_tree != node1 && left_tree != node2)
    return left_tree;

  Node* right_tree = Optimized(node->right_, node1, node2);
  if (right_tree != nullptr && right_tree != node1 && right_tree != node2)
    return right_tree;

  if ((left_tree == node1 && right_tree == node2) ||
      (left_tree == node2 && right_tree == node1)) {
    return node;
  } else if (left_tree != nullptr) { 
    return left_tree;
  } else if (right_tree != nullptr) {
    return right_tree;
  } else {
    return nullptr;
  }
}

#endif /* NODE_H_ */
