#include "BlackJack.h"
#include <climits>

int main(void)
{
  BlackJack* bj = new BlackJack();
  bj->InitGame();
  delete bj;
  return 0;
}
