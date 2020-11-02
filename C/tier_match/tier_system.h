#ifndef TIER_SYSTEM_H
#define TIER_SYSTEM_H

#include <stdlib.h>
#include "queue.h"

typedef struct {
    Tier tier;
    Queue* top;
    Queue* mid;
    Queue* side;
    Queue* bottom;
} TierSystem;

TierSystem* make_tier_system(Tier tier);

void delete_tier_system(TierSystem* ts);

void enqueue_pos(TierSystem* ts, Node* player);

bool is_match_ready(TierSystem* ts);

void start_match(TierSystem* ts);

void print_rem_tier_system(TierSystem* ts);

#endif
