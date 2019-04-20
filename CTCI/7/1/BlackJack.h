#ifndef BLACKJACK_H
#define BLACKJACK_H

#include "DeckOfCards.h"

class Player;

class BlackJack {
 public:
  BlackJack(Player* p1, Player* p2);
  void GiveCardToPlayer(Player* player);
  int CalculatePoint(Player* player);
  virtual ~BlackJack();

 private:
  void CalculatePointHelper(int nOfA, int current, int objective, int& closest);
  Deck* deck_;
  Player* p1_;
  Player* p2_;
};

class Player {
 public:
  Player(std::string name);
  void AddCard(PlayingCard* card);
  std::vector<PlayingCard*> GetHands();

 private:
  int score_;
  std::string name_;
  std::vector<PlayingCard*> hands_;
};

#endif /* BLACKJACK_H */
