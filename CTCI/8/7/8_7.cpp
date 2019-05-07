#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> PermNoDups(std::string str);
std::vector<std::string> PermNoDups(std::string str, size_t i, std::vector<std::string>& v);
std::string InsertChar(std::string str, char c, size_t pos);

int main(void)
{
  std::vector<std::string> o = PermNoDups("abcde");
  for (std::string str : o)
    std::cout << str << std::endl;
  return 0;
}

std::vector<std::string> PermNoDups(std::string str) {
  std::vector<std::string> v = {""};
  return PermNoDups(str, 0, v);
}

std::vector<std::string> PermNoDups(std::string str, size_t i, std::vector<std::string>& v) {
  if (i == str.length())
    return v;
  std::vector<std::string> n;
  for (std::string perm : v) {
    for (size_t j = 0; j <= perm.length(); ++j) {
      n.push_back(InsertChar(perm, str[i], j));
    }
  }
  return PermNoDups(str, i + 1, n);
}

std::string InsertChar(std::string str, char c, size_t pos) {
  str.insert(pos, std::string(1, c));
  return str;
}
