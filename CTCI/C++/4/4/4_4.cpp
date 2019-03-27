#include "BinaryTree.h"

int main(void)
{
  BinaryTree<int> *bt = new BinaryTree<int>();
  bt->root_ = new BinaryTree<int>::Node(1);
  bt->root_->left_ = new BinaryTree<int>::Node(2);
  bt->root_->right_ = new BinaryTree<int>::Node(3);
  bt->root_->left_->left_ = new BinaryTree<int>::Node(4);
  bt->root_->left_->right_ = new BinaryTree<int>::Node(5);
  bt->root_->right_->left_ = new BinaryTree<int>::Node(6);
  // bt->root_->left_->left_->left_ = new BinaryTree<int>::Node(7);

  std::cout << bt->CheckIfBalanced() << std::endl;

  delete bt;

  return 0;
}
