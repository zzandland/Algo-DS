#ifndef DECKOFCARDS_H
#define DECKOFCARDS_H

#include <iostream>
#include <string>
#include <vector>

class PlayingCard {
 public:
  PlayingCard(std::string rank, std::string court) : rank_(rank), court_(court) {}
  friend std::ostream& operator <<(std::ostream& ostr, const PlayingCard& card);

 private:
  std::string rank_;
  std::string court_;
};

class Deck {
 public:
  Deck();
  void PrintDeck();

 private:
  void InitDeck();
  void GenerateCourts(std::string rank);
  std::vector<PlayingCard*> deck_;
};

#endif /* DECKOFCARDS_H */
