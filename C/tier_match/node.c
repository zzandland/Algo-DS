#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "node.h"

Node* make_node(char* user_id, Tier tier, Pos pos) {
    Node* node = (Node*) malloc(sizeof(Node));
    node->user_id = user_id;
    node->tier = tier;
    node->pos = pos;
    node->next = NULL;
    return node;
}

void print_node(Node* node, bool print_tier) {
    printf("[%s, %s", node->user_id, str_pos(node->pos));
    if (print_tier) printf(", %s", str_tier(node->tier));
    printf("]");
}
