#include <iostream>
#include <map>
#include <vector>

std::vector<std::string> PermsWithDups(std::string str);
void PermsWithDups(std::map<char, int>& map, std::string perm,
                   std::vector<std::string>& output);
bool CheckEmpty(std::map<char, int>& map);

int main(void) {
  std::vector<std::string> o = PermsWithDups("abdbd");
  for (std::string s : o) std::cout << s << std::endl;
  return 0;
}

std::vector<std::string> PermsWithDups(std::string str) {
  std::map<char, int> map;
  std::vector<std::string> output;
  for (char c : str) map[c]++;
  PermsWithDups(map, "", output);
  return output;
}

void PermsWithDups(std::map<char, int>& map, std::string perm,
                   std::vector<std::string>& output) {
  if (CheckEmpty(map)) {
    output.push_back(perm);
    return;
  }
  for (auto it = map.begin(); it != map.end(); ++it) {
    if (it->second > 0) {
      --map[it->first];
      PermsWithDups(map, perm + it->first, output);
      ++map[it->first];
    }
  }
}

bool CheckEmpty(std::map<char, int>& map) {
  for (auto it = map.begin(); it != map. end(); ++it)
    if (it->second > 0) return false;
  return true;
}
