#include <climits>
#include <cmath>
#include "BlackJack.h"

BlackJackCard::BlackJackCard(Rank rank, Suit suit) : PlayingCard(rank, suit){};

BlackJackCard::~BlackJackCard() {}

int BlackJackCard::Score() {
  if (IsAce()) return 1;
  switch (rank_) {
    case 11:
    case 12:
    case 13:
      return 10;
      break;
    default:
      return rank_;
      break;
  }
}

bool BlackJackCard::IsAce() { return rank_ == 1; }

int BlackJackHand::Score() {
  int max_score = 0;
  GetPossibleHands(0, 0, max_score);
  return max_score;
}

void BlackJackHand::GetPossibleHands(size_t i, int score, int& max_score) {
  if (i == hand_.size()) {
    if (score < 22 && score > max_score) max_score = score;
    return;
  }
  BlackJackCard* card = hand_[i];
  if (card->IsAce()) {
    GetPossibleHands(i + 1, score + 1, max_score);
    GetPossibleHands(i + 1, score + 11, max_score);
  } else {
    GetPossibleHands(i + 1, score + card->Score(), max_score);
  }
}

BlackJack::BlackJack() : player_(new Player()), computer_(new Player()) {
  deck_ = new Deck<BlackJackCard>(false);
}

BlackJack::~BlackJack() {
  delete player_;
  delete computer_;
  player_ = computer_ = nullptr;
  deck_ = nullptr;
}

void BlackJack::InitGame() {
  bool ongoing = true;
  GiveCard(player_);
  GiveCard(computer_);
  do {
    ongoing = TakeTurn();
  } while (ongoing && (player_->Score() < 22 && player_->Score() != 0) &&
           (computer_->Score() < 22 && computer_->Score() != 0));
  int player_score = player_->Score();
  int computer_score = computer_->Score();
  std::cout << "You have ";
  player_->PrintHand();
  std::cout << "Computer has ";
  computer_->PrintHand();
  if ((player_score == 0 && computer_score == 0) ||
      player_score == computer_score)
    std::cout << "Draw";
  else if (player_score == 21)
    std::cout << "You lost";
  else if (computer_score == 21)
    std::cout << "You won";
  else if (player_score < computer_score)
    std::cout << "You lost";
  else if (player_score > computer_score)
    std::cout << "You won";
}

bool BlackJack::TakeTurn() {
  bool AI_drew_card = AITurn();
  std::cout << "You have ";
  player_->PrintHand();
  std::string input = "";
  std::cout << "\nDo you want to draw another card? (Y/N): ";
  if (!std::getline(std::cin, input)) exit(1);
  if (input == "Y" || input == "y") {
    GiveCard(player_);
  } else if ((input == "N" || input == "n") && !AI_drew_card) {
    return false;
  }
  return true;
}

bool BlackJack::AITurn() {
  if (computer_->Score() < 18) {
    std::cout << "Computer drew a card." << std::endl;
    GiveCard(computer_);
    return true;
  }
  return false;
}

void BlackJack::GiveCard(Player* player) {
  BlackJackCard* card = deck_->HandOutACard();
  player->AddCard(card);
}

void Player::AddCard(BlackJackCard* card) { hand_.AddCard(card); }

int Player::Score() { return hand_.Score(); }

void Player::PrintHand() { std::cout << hand_; }
