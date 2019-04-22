#ifndef BLACKJACK_H
#define BLACKJACK_H

#include "DeckOfCards.h"

class Player;

class BlackJackCard : public PlayingCard {
 public:
  BlackJackCard(Rank rank, Suit suit);
  virtual ~BlackJackCard();
  int Score();
  bool IsAce();
};

class BlackJackHand : public Hand<BlackJackCard> {
 public:
  int Score();
  void GetPossibleHands(size_t i, int score, int& max_score);
};

class BlackJack {
 public:
  BlackJack();
  virtual ~BlackJack();
  void InitGame();

 private:
  bool TakeTurn();
  bool AITurn();
  void GiveCard(Player* player);
  Deck<BlackJackCard>* deck_;
  Player* player_;
  Player* computer_;
};

class Player {
 public:
  void AddCard(BlackJackCard* card);
  int Score();
  void PrintHand();

 private:
  BlackJackHand hand_;
};

#endif /* BLACKJACK_H */
