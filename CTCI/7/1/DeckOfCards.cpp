#include "DeckOfCards.h"

std::ostream& operator<<(std::ostream& ostr, const PlayingCard& card) {
  ostr << card.court_ << " " << card.rank_;
  return ostr;
}

Deck::Deck() { InitDeck(); }

void Deck::PrintDeck() {
  for (PlayingCard* card : deck_) {
    std::cout << *card << std::endl;
  }
}

void Deck::InitDeck() {
  GenerateCourts("A");
  GenerateCourts("2");
  GenerateCourts("3");
  GenerateCourts("4");
  GenerateCourts("5");
  GenerateCourts("6");
  GenerateCourts("7");
  GenerateCourts("8");
  GenerateCourts("9");
  GenerateCourts("10");
  GenerateCourts("J");
  GenerateCourts("Q");
  GenerateCourts("K");
  deck_.push_back(new PlayingCard("Joker", "Black"));
  deck_.push_back(new PlayingCard("Joker", "Color"));
}

void Deck::GenerateCourts(std::string rank) {
  deck_.push_back(new PlayingCard(rank, "♥"));
  deck_.push_back(new PlayingCard(rank, "♦"));
  deck_.push_back(new PlayingCard(rank, "♣"));
  deck_.push_back(new PlayingCard(rank, "♠"));
}
