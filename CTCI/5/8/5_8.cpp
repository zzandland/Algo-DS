#include <vector>
#include <iostream>

std::vector<unsigned char> DrawLine(std::vector<unsigned char>& screen, int width, int x1, int x2, int y);

int main(void)
{
  std::vector<unsigned char> screen;
  for (int i = 0; i < 2000; ++i) {
    screen.push_back(0);
  }
  screen = DrawLine(screen, 160, 3, 5, 99);
  for (unsigned char byte : screen)
    std::cout << (int)byte << " ";
  return 0;
}

std::vector<unsigned char> DrawLine(std::vector<unsigned char>& screen, int width, int x1, int x2, int y) {
  int height = screen.size() / (width / 8);
  if (y >= height || x1 < 0 || x2 > width) {
    std::cerr << "Invalid inputs" << std::endl;
    exit(1);
  }
  int yIndex = (width / 8) * y;
  int x1Index = x1 / 8 + yIndex;
  int x1Offset = x1 % 8;
  int x2Index = x2 / 8 + yIndex;
  int x2Offset = x2 % 8;
  if (x1Index == x2Index) {
    screen[x1Index] = ((1 << (x2Offset - x1Offset)) - 1) << x1Offset;
  } else {
    screen[x1Index] = (1 << (8 - x1Offset)) - 1;
    for (int i = x1Index + 1; i < x2Index; ++i) {
      screen[i] = ~screen[i];
    }
    screen[x2Index] = (-1 << (8 - x2Offset));
  }
  return screen;
}
