#ifndef DECKOFCARDS_H
#define DECKOFCARDS_H

#include <iostream>
#include <string>
#include <vector>

class PlayingCard {
 public:
  PlayingCard(std::string rank, std::string court);
  std::vector<std::string> FaceUp();
  friend std::ostream& operator<<(std::ostream& ostr, const PlayingCard& card);

 private:
  std::string rank_;
  std::string court_;
  bool face_down_;
};

class Deck {
 public:
  Deck(bool joker_in);
  PlayingCard* HandOutACard();
  void PrintDeck() const;

 private:
  void InitDeck(bool joker_in);
  void GenerateCourts(std::string rank);
  void ShuffleDeck();
  void ReuseUsed();
  std::vector<PlayingCard*> unknown_deck_;
  std::vector<PlayingCard*> used_deck_;
};

#endif /* DECKOFCARDS_H */
