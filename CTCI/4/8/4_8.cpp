#include "BinaryTree.h"

int main(void)
{
  Node<char>* root = new Node<char>('A');
  root->left_ = new Node<char>('B');
  root->left_->left_ = new Node<char>('D');
  root->left_->right_ = new Node<char>('E');
  root->left_->right_->left_ = new Node<char>('F');
  root->left_->right_->right_ = new Node<char>('G');
  root->left_->right_->right_->left_ = new Node<char>('H');
  root->right_ = new Node<char>('C');
  root->right_->right_ = new Node<char>('O');

  Node<char>* node1 = root->left_->right_->left_;
  Node<char>* node2 = root->left_->right_->right_->left_;

  Node<char>* ans = root->CommonAncestor(root, node1, node2);
  std::cout << ans->data_ << std::endl;

  delete root;
  return 0;
}
