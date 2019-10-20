#include <stdio.h>
#include <stdlib.h>

struct Node {
  int key;
  int val;
  struct Node* next;
};

struct HashTable {
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

struct Node* generateNode(int key, int val) {
  struct Node* n = (struct Node*)(malloc(sizeof(struct Node)));
  n->key = key;
  n->val = val;
  return n;
}

struct HashTable* generateHashTable(int size) {
  struct HashTable* set = (struct HashTable*)(malloc(sizeof(struct HashTable)));
  set->size = size;
  set->arr = (struct Node**)(malloc(sizeof(struct Node*) * size));
  return set;
}

struct Node* checkHashTable(struct HashTable *ht, int key) {
  int mod = hashIndex(key) % ht->size;
  struct Node* i = ht->arr[mod];
  while (i) {
    if (i->key == key) return i;
    i = i->next;
  }
  return NULL;
}

void insertToHashTable(struct HashTable *ht, int key, int val) {
  struct Node* i = checkHashTable(ht, key);
  if (i != NULL) {
    i->val = val;
    return;
  }
  int mod = hashIndex(key) % ht->size;
  i = ht->arr[mod];
  if (!i) {
    ht->arr[mod] = generateNode(key, val);
    return;
  } 
  while (i->next)
    i = i->next;
  i->next = generateNode(key, val);
}

int main(int argc, char *argv[]) {
  struct HashTable* ht = generateHashTable(997);
  insertToHashTable(ht, 35, 2);
  printf("%d\n", checkHashTable(ht, 35)->val);
  insertToHashTable(ht, 35, 17);
  printf("%d\n", checkHashTable(ht, 35)->val);
  insertToHashTable(ht, 2, 358);
  printf("%d\n", checkHashTable(ht, 2)->val);
  return 0;
}
