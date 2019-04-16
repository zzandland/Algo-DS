#include "BST.h"

int main(void)
{
  BST<int>* bst = new BST<int>();
  bst->Insert(5);
  bst->Insert(3);
  bst->Insert(1);
  bst->Insert(4);
  bst->Insert(7);
  bst->Insert(9);
  bst->Iterate();
  BST<int>::Node* n = bst->RandomNode();
  std::cout << n->data_ << " " << n->nLeft << " " << n->nRight;
  delete bst;
  return 0;
}
