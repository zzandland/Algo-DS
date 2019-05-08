#include <iostream>
#include <vector>

enum class Color { White, Red, Yellow, Orange };

struct Point {
  int y;
  int x;
};

class Screen {
 public:
  Screen(int y, int x)
      : s_(std::vector<std::vector<Color>>(y, std::vector<Color>(x))),
        height_(y),
        width_(x) {
    for (int i = 0; i < y; ++i)
      for (int j = 0; j < x; ++j) s_[i][j] = Color::White;
  }

  void PaintFill(Point p, Color c) {
    if (s_[p.y][p.x] == c) return;
    return PaintFill(p, s_[p.y][p.x], c);
  };

  void PaintFill(Point p, Color o, Color c) {
    if (p.y >= height_ || p.y < 0 || p.x >= width_ || p.x < 0) return;
    if (s_[p.y][p.x] == o) {
      s_[p.y][p.x] = c;
      PaintFill({p.y - 1, p.x}, o, c);
      PaintFill({p.y + 1, p.x}, o, c);
      PaintFill({p.y, p.x - 1}, o, c);
      PaintFill({p.y, p.x + 1}, o, c);
    }
  };

  std::vector<std::vector<Color>> s_;
  int height_;
  int width_;
};

int main(void) {
  Screen* s = new Screen(100, 500);
  std::cout << (int)s->s_[2][2];
  s->PaintFill({3, 2}, Color::Orange);
  std::cout << (int)s->s_[3][1];
  return 0;
}
