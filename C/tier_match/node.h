#ifndef NODES_H
#define NODES_H

#include "enums.h"

typedef struct Node {
    char* user_id;
    Tier tier;
    Pos pos;
    struct Node* next;
} Node;

Node* make_node(char* user_id, Tier tier, Pos pos);

void print_node(Node* node, bool print_tier);

#endif
