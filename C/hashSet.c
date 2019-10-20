#include <stdio.h>
#include <stdlib.h>

struct Node {
  int key;
  struct Node* next;
};

struct HashSet {
  int size;
  struct Node** arr;
};

unsigned long hash(char const *str) {
  unsigned long hash = 5381;
  while (*str++)
    hash = hash * 33 + *str;
  return hash;
}

unsigned long hashIndex(int key) {
  char strKey[32];
  sprintf(strKey, "%d", key);
  return hash(strKey);
}

struct Node* generateNode(int key) {
  struct Node* n = (struct Node*)(malloc(sizeof(struct Node)));
  n->key = key;
  return n;
}

struct HashSet* generateHashSet(int size) {
  struct HashSet* set = (struct HashSet*)(malloc(sizeof(struct HashSet)));
  set->size = size;
  set->arr = (struct Node**)(malloc(sizeof(struct Node*) * size));
  return set;
}

void insertToHashSet(struct HashSet *hs, int key) {
  int mod = hashIndex(key) % hs->size;
  struct Node* i = hs->arr[mod];
  if (!i) {
    hs->arr[mod] = generateNode(key);
    return;
  } 
  while (i->next) 
    i = i->next;
  i->next = generateNode(key);
}

int checkHashSet(struct HashSet *hs, int key) {
  int mod = hashIndex(key) % hs->size;
  struct Node* i = hs->arr[mod];
  while (i) {
    if (i->key == key) return 1;
    i = i->next;
  }
  return 0;
}

int main(int argc, char *argv[]) {
  struct HashSet* hs = generateHashSet(1);
  insertToHashSet(hs, 920);
  insertToHashSet(hs, 15);
  printf("%d", checkHashSet(hs, 15));
  return 0;
}
