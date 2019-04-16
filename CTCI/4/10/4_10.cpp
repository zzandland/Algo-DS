#include "BinaryTree.h"

int main(void)
{
  BinaryTree<int>* bst1 = new BinaryTree<int>();
  bst1->root_ = new BinaryTree<int>::Node(5);
  bst1->root_->left_ = new BinaryTree<int>::Node(3);
  bst1->root_->right_ = new BinaryTree<int>::Node(2);
  bst1->root_->right_->left_ = new BinaryTree<int>::Node(10);
  bst1->root_->right_->right_ = new BinaryTree<int>::Node(8);

  BinaryTree<int>* bst2 = new BinaryTree<int>();
  bst2->root_ = new BinaryTree<int>::Node(5);
  bst2->root_->left_ = new BinaryTree<int>::Node(3);
  bst2->root_->right_ = new BinaryTree<int>::Node(2);

  std::cout << bst1->CheckSubtreeMemory(bst2);

  delete bst1;
  delete bst2;
  return 0;
}
