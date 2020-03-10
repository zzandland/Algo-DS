#include <iostream>
#include <set>
#include <vector>

using namespace std;

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
    vector<Node*> children_;

    Node(char val) : val_(val), end_(false), children_(27){};

    ~Node() {
      for (Node* n : children_) {
        if (n != nullptr) delete n;
      }
    }
  };
  Node* root_;

  Trie(vector<string>& words, map<string, int>& word_map)
      : root_(new Node(' ')) {
    for (string word : words) {
      InsertWord(word);
      if (word_map.find(word) == word_map.end())
        word_map.insert({word, 1});
      else
        ++word_map[word];
    }
  };

  ~Trie() { delete root_; }

  void InsertWord(string word) {
    Node* n = root_;
    for (size_t i = 0; i < word.length(); ++i) {
      int index = word[i] - 'a';
      if (n->children_[index] == nullptr)
        n->children_[index] = new Node(word[i]);
      n = n->children_[index];
    }
    n->end_ = true;
  }

  string FindWord(string s, size_t i) {
    string word = "";
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

  void IterateTrie(Node* n, string s) {
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
  vector<vector<string>> getPerm(vector<string>& words) {
    vector<vector<string>> output, prev;
    if (words.size() == 1) {
      output.push_back(words);
      return output;
    }
    string word = words.back();
    words.pop_back();
    prev = getPerm(words);
    for (auto perm : prev) {
      for (int i = 0; i <= perm.size(); ++i) {
        vector<string> cpy = perm;
        cpy.insert(cpy.begin() + i, word);
        output.push_back(cpy);
      }
    }
    return output;
  }

  set<string> getPermStr(vector<vector<string>>& perms) {
    set<string> output;
    for (auto perm : perms) {
      string s;
      for (auto st : perm) {
        s += st;
      }
      output.insert(s);
    }
    return output;
  }

  vector<int> findSubstring(string s, vector<string>& words) {
    if (words.size() == 0) {
      return vector<int>();
    }
    int len = words.size() * (*words.begin()).length();
    if (s.length() < len) {
      return vector<int>();
    }
    vector<vector<string>> perms = getPerm(words);
    set<string> strs = getPermStr(perms);
    vector<int> output;
    for (int i = 0; i < s.length() - len + 1; ++i) {
      if (strs.count(s.substr(i, len))) {
        output.push_back(i);
      }
    }
    return output;
  }
};
