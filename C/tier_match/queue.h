#ifndef QUEUE_H
#define QUEUE_H

#include "node.h"

typedef struct {
    Node* front;
    Node* rear;
    int size;
} Queue;

Queue* make_queue();

void delete_queue(Queue* q);

bool is_empty(Queue* q);

void enqueue(Queue* q, Node* player);

Node* dequeue(Queue* q);

void print_opponents(Queue* q);

void print_rem_queue(Queue* q);

#endif
