#include "BST.h"

int main(void) {
  std::vector<int> list;

  for (int i = 1; i <= 100000; ++i) {
    list.push_back(i);
  }

  BST<int> *bst = new BST<int>(list);
  std::cout << bst->GetMaxHeight();
  return 0;
}
