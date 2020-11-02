#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "node.h"
#include "queue.h"

Queue* make_queue() {
    Queue* q = (Queue*) malloc(sizeof(Queue));
    q->front = NULL;
    q->rear = NULL;
    q->size = 0;
    return q;
}

void delete_queue(Queue *q) {
    while (!is_empty(q)) free(dequeue(q));
    free(q);
}

bool is_empty(Queue* q) {
    return q->size == 0;
}

void enqueue(Queue* q, Node* player) {
    if (!is_empty(q)) q->rear->next = player;
    q->rear = player;
    if (!q->front) q->front = player;
    q->size++;
};

Node* dequeue(Queue* q) {
    if (is_empty(q)) {
        fprintf(stderr, "Queue is empty");
        exit(1);
    }

    Node* removeNode = q->front;
    q->front = q->front->next;
    if (is_empty(q)) q->rear = NULL;
    q->size--;

    return removeNode;
}

void print_opponents(Queue* q) {
    Node* t1 = dequeue(q);
    Node* t2 = dequeue(q);
    print_node(t1, false); 
    printf("            ");
    print_node(t2, false); 
    printf("\n");
    free(t1);
    free(t2);
}

void print_rem_queue(Queue* q) {
    Node* p = q->front;
    while (p) {
        print_node(p, true);
        printf(" ");
        p = p->next;
    }
}
