#include <iostream>
#include <vector>
#include <set>
#include <bits/stdc++.h>

struct Box {
  int w; int l; int h;
};

bool CanStackAonB(Box* a, Box* b) {
  return b->w > a->w && b->l > a->l;
}

bool Comparator(Box* a, Box* b) {
  return b->h < a->h;
};

int SoB(std::vector<Box*>& boxes, int i, int j, std::vector<std::vector<int>>& dp) {
  if (i >= (int)boxes.size()) return 0;
  if (dp[i][j + 1] == 0) {
    int with = 0;
    if (j == -1 || CanStackAonB(boxes[i], boxes[j])) {
      with = boxes[i]->h + SoB(boxes, i + 1, i, dp);
    }
    int without = SoB(boxes, i + 1, j, dp);
    dp[i][j + 1] = std::max(with, without);
  }
  return dp[i][j + 1];
}

int SoB(std::vector<Box*>& boxes) {
  std::sort(boxes.begin(), boxes.end(), Comparator);
  int box_len = boxes.size();
  std::vector<std::vector<int>> dp(box_len, std::vector<int>(box_len));
  return SoB(boxes, 0, -1, dp);
};

int SoB_BU(std::vector<Box*>& boxes) {
  std::sort(boxes.begin(), boxes.end(), Comparator);
};

// bool CanStackAonB(Box* a, Box* b) {
  // return (b->h > a->h && b->w > a->w && b->l > a->l);
// }

// int SoB(Box* curr, std::vector<Box*>& boxes, std::set<Box*>& box_set, int h) {
  // int boxes_len = boxes.size();
  // if ((int)box_set.size() == boxes_len) return h;
  // int max_h = h;
  // for (int i = 0; i < boxes_len; ++i) {
    // Box* b = boxes[i];
    // if (box_set.find(b) != box_set.end() || curr == b) continue;
    // if (CanStackAonB(b, curr)) {
      // box_set.insert(b);
      // max_h = std::max(max_h, SoB(b, boxes, box_set, h + b->h));
      // box_set.erase(b);
    // }
  // }
  // return std::max(h, max_h);
// }

// int SoB(std::vector<Box*>& boxes) {
  // int output = 0;
  // std::set<Box*> box_set;
  // for (int i = 0; i < (int)boxes.size(); ++i)
    // output = std::max(output, SoB(boxes[i], boxes, box_set, boxes[i]->h));
  // return output;
// }

int main(void)
{
  Box b1 = {1, 5, 2};
  Box b2 = {1, 3, 3};
  Box b3 = {3, 5, 15};
  Box b4 = {2, 3, 5};
  Box b5 = {10, 8, 8};
  Box b6 = {25, 10, 10};
  std::vector<Box*> b = {&b1, &b2, &b3, &b4, &b5, &b6};
  std::cout << SoB(b);
  return 0;
}
