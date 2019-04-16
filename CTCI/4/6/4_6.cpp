#include "BST.h"

int main(void) {
  BST<int>* bst = new BST<int>();
  bst->Insert(5);
  bst->Insert(2);
  bst->Insert(1);
  bst->Insert(4);
  bst->Insert(8);
  bst->Insert(7);
  bst->Insert(6);
  bst->Insert(10);

  std::cout << bst->Predecessor(6)->data_ << " -> "
            << "6"
            << " -> " << bst->Successor(6)->data_ << std::endl;

  bst->Delete(7);

  std::cout << bst->Successor(6)->data_;

  // delete bst;
  return 0;
}
