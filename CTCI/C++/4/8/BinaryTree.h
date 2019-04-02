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

  bool FirstCommonAncestor(Node* node, Node* node1, Node* node2, Node*& common_anc);
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
bool Node<T>::FirstCommonAncestor(Node* node, Node* node1, Node* node2, Node*& common_anc) {
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

#endif /* NODE_H_ */
