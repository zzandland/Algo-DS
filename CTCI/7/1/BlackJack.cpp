#include <climits>
#include <cmath>
#include "BlackJack.h"

BlackJack::BlackJack(Player* p1, Player* p2) : p1_(p1), p2_(p2) {
  deck_ = new Deck(false);
}

BlackJack::~BlackJack() {
  delete deck_;
  p1_ = p2_ = nullptr;
}

void BlackJack::GiveCardToPlayer(Player* player) {
  PlayingCard* card = deck_->HandOutACard();
  player->AddCard(card);
}

int BlackJack::CalculatePoint(Player* player) {
  std::vector<PlayingCard*> hand = player->GetHands();
  int nOfA = 0;
  int total = 0;
  for (PlayingCard* card : hand) {
    std::string rank = card->FaceUp()[1];
    if (rank == "A")
      ++nOfA;
    else if (rank == "2")
      total += 2;
    else if (rank == "3")
      total += 3;
    else if (rank == "4")
      total += 4;
    else if (rank == "5")
      total += 5;
    else if (rank == "6")
      total += 6;
    else if (rank == "7")
      total += 7;
    else if (rank == "8")
      total += 8;
    else if (rank == "9")
      total += 9;
    else if (rank == "10")
      total += 10;
    else if (rank == "J" || rank == "Q" || rank == "K")
      total += 10;
  }
  int score_A = -1;
  if (total > 21) {
    score_A = nOfA;
  } else {
    CalculatePointHelper(nOfA, 0, 21 - total, score_A);
  }
  return total + score_A;
}

void BlackJack::CalculatePointHelper(int nOfA, int current, int objective,
                                     int& closest) {
  if (nOfA == 0) {
    if (current <= objective && current > closest) closest = current;
    return;
  }
  if (objective == closest) return;
  CalculatePointHelper(nOfA - 1, current + 11, objective, closest);
  CalculatePointHelper(nOfA - 1, current + 1, objective, closest);
}

Player::Player(std::string name) : name_(name) { score_ = 0; }

void Player::AddCard(PlayingCard* card) {
  hands_.push_back(card);
}

std::vector<PlayingCard*> Player::GetHands() { return hands_; }
