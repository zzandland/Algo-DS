#include "BlackJack.h"
#include <climits>

int main(void)
{
  Player* p1 = new Player("David");
  Player* p2 = new Player("Sarah");
  BlackJack* bj = new BlackJack(p1, p2);
  delete bj;
  delete p1;
  delete p2;
  return 0;
}
