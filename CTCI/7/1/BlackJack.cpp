#include <climits>
#include <cmath>
#include "BlackJack.h"

BlackJack::BlackJack() : p1_(new Player()), p2_(new Player()) {
  deck_ = new Deck(false);
}

BlackJack::~BlackJack() {
  delete deck_;
  delete p1_;
  delete p2_;
  p1_ = p2_ = nullptr;
  deck_ = nullptr;
}

void BlackJack::InitGame() {
  bool ongoing = true;
  GiveCardToPlayer(p1_);
  GiveCardToPlayer(p2_);
  while (ongoing && CalculatePoint(p1_) < 22 && CalculatePoint(p2_) < 22)
    ongoing = TakeTurn();
  int p1_total = CalculatePoint(p1_);
  int p2_total = CalculatePoint(p2_);
  std::cout << "You have ";
  p1_->PrintHands();
  std::cout << "Computer has ";
  p2_->PrintHands();
  if ((p1_total > 21 && p2_total > 21) || p1_total == p2_total)
    std::cout << "Draw";
  else if (p1_total > 21)
    std::cout << "You lost";
  else if (p2_total > 21)
    std::cout << "You won";
  else if (p1_total < p2_total)
    std::cout << "You lost";
  else if (p1_total > p2_total)
    std::cout << "You won";
}

bool BlackJack::TakeTurn() {
  bool AI_drew_card = AITurn();
  std::cout << "You have ";
  p1_->PrintHands();
  std::string input = "";
  std::cout << "\nDo you want to draw another card? (Y/N): ";
  if (!std::getline(std::cin, input)) exit(1);
  if (input == "Y" || input == "y") {
    GiveCardToPlayer(p1_);
  } else if ((input == "N" || input == "n") && !AI_drew_card) {
    return false;
  }
  return true;
}

bool BlackJack::AITurn() {
  if (CalculatePoint(p2_) < 18) {
    std::cout << "Computer drew a card." << std::endl;
    GiveCardToPlayer(p2_);
    return true;
  }
  return false;
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

Player::Player() { score_ = 0; }

void Player::AddCard(PlayingCard* card) { hands_.push_back(card); }

std::vector<PlayingCard*> Player::GetHands() { return hands_; }

void Player::PrintHands() {
  for (PlayingCard* card : hands_) std::cout << *card << " ";
  std::cout << std::endl;
}
