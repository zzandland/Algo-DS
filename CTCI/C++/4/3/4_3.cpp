#include <random>
#include "BST.h"

int main(void) { 
  BST<int> *tree = new BST<int>();

  std::default_random_engine generator;
  std::uniform_int_distribution<int> ran_num(1, 3000);
  tree->Insert(1500);
  for (int i = 0; i < 100; ++i) {
    tree->Insert(ran_num(generator));
  }

  std::vector<BST<int>::ListNode*> arr = tree->ListOfDepths();

  for (size_t i = 0; i < arr.size(); ++i) {
    arr[i]->PrintList();
  }

  return 0; 
}
