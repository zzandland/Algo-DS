#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "node.h"
#include "queue.h"
#include "tier_system.h"

TierSystem* make_tier_system(Tier tier) {
    TierSystem* ts = (TierSystem*) malloc(sizeof(TierSystem));
    ts->tier = tier;
    ts->top = make_queue();
    ts->mid = make_queue();
    ts->side = make_queue();
    ts->bottom = make_queue();
    return ts;
}

void delete_tier_system(TierSystem* ts) {
    delete_queue(ts->top);
    delete_queue(ts->mid);
    delete_queue(ts->side);
    delete_queue(ts->bottom);
    free(ts);
}

void enqueue_pos(TierSystem* ts, Node* player) {
    switch (player->pos) {
        case top:
            enqueue(ts->top, player);
            break;
        case mid:
            enqueue(ts->mid, player);
            break;
        case side:
            enqueue(ts->side, player);
            break;
        case bottom:
            enqueue(ts->bottom, player);
            break;
    }
}

bool is_match_ready(TierSystem* ts) {
    return (ts->top->size >= 2 &&
            ts->mid->size >= 2 &&
            ts->side->size >= 2) &&
            ts->bottom->size >= 2;
}

void start_match(TierSystem* ts) {
    printf("%s\n", str_tier(ts->tier));
    printf("치킨              vs             피자\n");
    print_opponents(ts->top);
    print_opponents(ts->mid);
    print_opponents(ts->side);
    print_opponents(ts->bottom);
    printf("\n");
}

void print_rem_tier_system(TierSystem* ts) {
    print_rem_queue(ts->top);
    print_rem_queue(ts->mid);
    print_rem_queue(ts->side);
    print_rem_queue(ts->bottom);
}
