#include <algorithm>
#include "DeckOfCards.h"

PlayingCard::PlayingCard(std::string rank, std::string court) : rank_(rank), court_(court) {
  face_down_ = true;
}

std::vector<std::string> PlayingCard::FaceUp() {
  face_down_ = false;
  std::vector<std::string> pair = {court_, rank_};
  return pair;
}

std::ostream& operator<<(std::ostream& ostr, const PlayingCard& card) {
  ostr << card.court_ << card.rank_;
  return ostr;
}

Deck::Deck(bool joker_in) { InitDeck(joker_in); }

PlayingCard* Deck::HandOutACard() {
  if (unknown_deck_.empty()) ReuseUsed();
  PlayingCard* out = unknown_deck_.back();
  unknown_deck_.pop_back();
  used_deck_.push_back(out);
  return out;
}

void Deck::PrintDeck() const {
  for (PlayingCard* card : unknown_deck_) {
    std::cout << *card << std::endl;
  }
}

void Deck::InitDeck(bool joker_in) {
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
  if (joker_in) {
    unknown_deck_.push_back(new PlayingCard("Joker", "Black"));
    unknown_deck_.push_back(new PlayingCard("Joker", "Color"));
  }
  ShuffleDeck();
}

void Deck::GenerateCourts(std::string rank) {
  unknown_deck_.push_back(new PlayingCard(rank, "♥"));
  unknown_deck_.push_back(new PlayingCard(rank, "♦"));
  unknown_deck_.push_back(new PlayingCard(rank, "♣"));
  unknown_deck_.push_back(new PlayingCard(rank, "♠"));
}

void Deck::ShuffleDeck() {
  std::srand(time(0));
  for (int i = unknown_deck_.size(); i > 1; --i) {
    int j = std::rand() % i;
    std::swap(unknown_deck_[i - 1], unknown_deck_[j]);
  }
}

void Deck::ReuseUsed() {
  std::cout << "Reuse" << std::endl;
  unknown_deck_.insert(unknown_deck_.end(), used_deck_.begin(),
                       used_deck_.end());
  ShuffleDeck();
  used_deck_.clear();
}
