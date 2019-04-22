#ifndef DECKOFCARDS_H
#define DECKOFCARDS_H

#include <iostream>
#include <string>
#include <vector>

enum class Rank {
  JOKER,
  ACE,
  TWO,
  THREE,
  FOUR,
  FIVE,
  SIX,
  SEVEN,
  EIGHT,
  NINE,
  TEN,
  JACK,
  QUEEN,
  KING
};

class PlayingCard {
 public:
  enum Suit { CLUB, DIAMOND, HEART, SPADE };

  PlayingCard(Rank rank, Suit suit);
  operator Suit();
  std::string to_string() const;
  virtual int Score() = 0;
  friend std::ostream& operator<<(std::ostream& ostr, const PlayingCard& card);

 protected:
  int rank_;  // Jack = 11, Queen = 12, King = 13, Joker = 14
  Suit suit_;
};

template <class T>
class Deck {
 public:
  Deck(bool joker_in);
  virtual ~Deck();
  T* HandOutACard();

 private:
  void InitDeck(bool joker_in);
  void GenerateCourts(Rank rank);
  void ShuffleDeck();
  void Reshuffle();
  std::vector<T*> deck_;
  size_t used_index_;
};

template <class T>
Deck<T>::Deck(bool joker_in) : used_index_(0) {
  InitDeck(joker_in);
}

template <class T>
Deck<T>::~Deck() {
  for (T* card : deck_) delete card;
}

template <class T>
T* Deck<T>::HandOutACard() {
  if (used_index_ == deck_.size()) Reshuffle();
  return deck_[used_index_++];
}

template <class T>
void Deck<T>::InitDeck(bool joker_in) {
  GenerateCourts(Rank::ACE);
  GenerateCourts(Rank::TWO);
  GenerateCourts(Rank::THREE);
  GenerateCourts(Rank::FOUR);
  GenerateCourts(Rank::FIVE);
  GenerateCourts(Rank::SIX);
  GenerateCourts(Rank::SEVEN);
  GenerateCourts(Rank::EIGHT);
  GenerateCourts(Rank::NINE);
  GenerateCourts(Rank::TEN);
  GenerateCourts(Rank::JACK);
  GenerateCourts(Rank::QUEEN);
  GenerateCourts(Rank::KING);
  if (joker_in) {
    deck_.push_back(new T(Rank::JOKER, PlayingCard::CLUB));
    deck_.push_back(new T(Rank::JOKER, PlayingCard::DIAMOND));
  }
  ShuffleDeck();
}

template <class T>
void Deck<T>::GenerateCourts(Rank rank) {
  deck_.push_back(new T(rank, PlayingCard::HEART));
  deck_.push_back(new T(rank, PlayingCard::DIAMOND));
  deck_.push_back(new T(rank, PlayingCard::CLUB));
  deck_.push_back(new T(rank, PlayingCard::HEART));
}

template <class T>
void Deck<T>::ShuffleDeck() {
  std::srand(time(0));
  for (int i = deck_.size(); i > 1; --i) {
    int j = std::rand() % i;
    std::swap(deck_[i - 1], deck_[j]);
  }
}

template <class T>
void Deck<T>::Reshuffle() {
  ShuffleDeck();
  used_index_ = 0;
}

template <class T>
class Hand;

template <typename T>
std::ostream& operator<<(std::ostream& ostr, const Hand<T>& hand);

template <class T>
class Hand {
 public:
  virtual ~Hand();
  void AddCard(T* card);
  int Score();
  friend std::ostream& operator<<<>(std::ostream& ostr, const Hand<T>& hand);

 protected:
  std::vector<T*> hand_;
};

template <class T>
Hand<T>::~Hand() {
  for (T* card : hand_) delete card;
};

template <class T>
void Hand<T>::AddCard(T* card) {
  hand_.push_back(card);
}

template <class T>
int Hand<T>::Score() {
  int total = 0;
  for (T* card : hand_) total += card->Score();
  return total;
}

template <class T>
std::ostream& operator<<(std::ostream& ostr, const Hand<T>& hand) {
  for (T* card : hand.hand_) ostr << *card << " ";
  ostr << std::endl;
  return ostr;
}

#endif /* DECKOFCARDS_H */
