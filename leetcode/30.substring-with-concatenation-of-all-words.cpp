#include <iostream>
#include <map>
#include <vector>

/*
 * @lc app=leetcode id=30 lang=cpp
 *
 * [30] Substring with Concatenation of All Words
 *
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (23.38%)
 * Total Accepted:    128.9K
 * Total Submissions: 551K
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * You are given a string, s, and a list of words, words, that are all of the
 * same length. Find all starting indices of substring(s) in s that is a
 * concatenation of each word in words exactly once and without any intervening
 * characters.
 *
 * Example 1:
 *
 *
 * Input:
 * ⁠ s = "barfoothefoobarman",
 * ⁠ words = ["foo","bar"]
 * Output: [0,9]
 * Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
 * respectively.
 * The output order does not matter, returning [9,0] is fine too.
 *
 *
 * Example 2:
 *
 *
 * Input:
 * ⁠ s = "wordgoodgoodgoodbestword",
 * ⁠ words = ["word","good","best","word"]
 * Output: []
 *
 *
 */
class Trie {
 public:
  class Node {
   public:
    char val_;
    bool end_;
    std::vector<Node*> children_;

    Node(char val) : val_(val), end_(false), children_(27){};

    ~Node() {
      for (Node* n : children_) {
        if (n != nullptr) delete n;
      }
    }
  };
  Node* root_;

  Trie(std::vector<std::string>& words, std::map<std::string, int>& word_map)
      : root_(new Node(' ')) {
    for (std::string word : words) {
      InsertWord(word);
      if (word_map.find(word) == word_map.end())
        word_map.insert({word, 1});
      else
        ++word_map[word];
    }
  };

  ~Trie() { delete root_; }

  void InsertWord(std::string word) {
    Node* n = root_;
    for (size_t i = 0; i < word.length(); ++i) {
      int index = word[i] - 'a';
      if (n->children_[index] == nullptr)
        n->children_[index] = new Node(word[i]);
      n = n->children_[index];
    }
    n->end_ = true;
  }

  std::string FindWord(std::string s, size_t i) {
    std::string word = "";
    Node* n = root_;
    for (; i < s.size(); ++i) {
      if (n->end_) return word;
      int index = s[i] - 'a';
      if (n->children_[index] == nullptr)
        return "";
      else {
        word += s[i];
        n = n->children_[index];
      }
    }
    return word;
  }

  void IterateTrie(Node* n, std::string s) {
    if (n == nullptr) return;
    s += n->val_;
    if (n->end_) {
      return;
    }     
    for (Node* n_ : n->children_)
      IterateTrie(n_, s);
  }
};

class Solution {
 public:
  std::vector<int> findSubstring(std::string s,
                                 std::vector<std::string>& words) {
    std::vector<int> output;
    if (words.size() == 0 || s.length() == 0) return output;
    std::map<std::string, int> word_map_origin;
    Trie* trie = new Trie(words, word_map_origin);
    for (size_t i = 0; i < s.length(); ++i) {
      std::map<std::string, int> word_map = word_map_origin;
      int j = i;
      while (!word_map.empty()) {
        std::string found = trie->FindWord(s, j);
        if (found != "") {
          if (word_map.find(found) == word_map.end()) break;
          word_map[found] -= 1;
          if (word_map[found] <= 0) word_map.erase(found);
          j += found.length();
        } else {
          break;
        }
      }
      if (word_map.empty()) output.push_back(i);
    }
    delete trie;
    return output;
  }
};
