#include <random>
#include "BinaryTree.h"

int main(void)
{
  BinaryTree<int> *bt1 = new BinaryTree<int>();
  std::default_random_engine generator;
  std::uniform_int_distribution<int> ran_num(1, 3000);

  for (int i = 0; i < 100; ++i)
    bt1->InsertBST(ran_num(generator));

  // bt1->InOrderDFS(bt1->root_);
  std::cout << std::endl << bt1->ValidateBST() << std::endl;

  delete bt1;

  return 0;
}
