#ifndef BLACKJACK_H
#define BLACKJACK_H

#include "DeckOfCards.h"

class Player;

class BlackJack {
 public:
  BlackJack();
  virtual ~BlackJack();
  void InitGame();

 private:
  bool TakeTurn();
  bool AITurn();
  void GiveCardToPlayer(Player* player);
  int CalculatePoint(Player* player);
  void CalculatePointHelper(int nOfA, int current, int objective, int& closest);
  Deck* deck_;
  Player* p1_;
  Player* p2_;
};

class Player {
 public:
  Player();
  void AddCard(PlayingCard* card);
  std::vector<PlayingCard*> GetHands();
  void PrintHands();

 private:
  int score_;
  std::vector<PlayingCard*> hands_;
};

#endif /* BLACKJACK_H */
