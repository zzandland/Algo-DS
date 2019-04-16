#include "BST.h"

int IntComparator(int val1, int val2);

int main(void) {
  int (*int_cmpr)(int val1, int val2);
  int_cmpr = &IntComparator;

  BST<int>* bst = new BST<int>(5, int_cmpr);
  bst->InsertNode(3);
  bst->InsertNode(7);
  bst->InsertNode(1);
  bst->InsertNode(4);
  bst->InsertNode(6);
  bst->InsertNode(9);
  // std::cout << bst->ValidateBST() << std::endl;

  std::vector<std::list<int>> seqs = bst->Sequences2();
  for (std::list<int> seq : seqs) {
    for (int data : seq)
      std::cout << data << " ";
    std::cout << std::endl;
  }

  delete bst;
  return 0;
}

int IntComparator(int val1, int val2) {
  return (val1 < val2) ? 1 : (val2 < val1) ? -1 : 0;
}
