#include "BinaryTree.h"

int main(void)
{
  BinaryTree<int>* bst = new BinaryTree<int>();
  bst->root_ = new BinaryTree<int>::Node(10);
  bst->root_->left_ = new BinaryTree<int>::Node(5);
  bst->root_->left_->left_ = new BinaryTree<int>::Node(3);
  bst->root_->left_->left_->left_ = new BinaryTree<int>::Node(3);
  bst->root_->left_->left_->right_ = new BinaryTree<int>::Node(-2);
  bst->root_->left_->right_ = new BinaryTree<int>::Node(2);
  bst->root_->left_->right_->right_ = new BinaryTree<int>::Node(1);
  bst->root_->right_ = new BinaryTree<int>::Node(-3);
  bst->root_->right_->right_ = new BinaryTree<int>::Node(11);

  std::cout << bst->PathSum(11) << std::endl;

  delete bst;
  return 0;
}
