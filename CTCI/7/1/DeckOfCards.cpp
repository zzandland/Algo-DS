#include <algorithm>
#include "DeckOfCards.h"

PlayingCard::PlayingCard(Rank rank, Suit suit)
    : rank_((int)rank), suit_(suit) {}

PlayingCard::operator Suit() { return suit_; }

std::string PlayingCard::to_string() const {
  std::string rank, suit;

  switch (rank_) {
    case 0:
      rank = "Joker";
      break;
    case 1:
      rank = "A";
      break;
    case 11:
      rank = "J";
      break;
    case 12:
      rank = "Q";
      break;
    case 13:
      rank = "K";
      break;
    default:
      rank = std::to_string(rank_);
  }

  switch (suit_) {
    case CLUB:
      suit = "♣";
      break;
    case DIAMOND:
      suit = "♦";
      break;
    case HEART:
      suit = "♥";
      break;
    case SPADE:
      suit = "♠";
      break;
  }

  return rank + suit;
}

std::ostream& operator<<(std::ostream& ostr, const PlayingCard& card) {
  ostr << card.to_string();
  return ostr;
}
