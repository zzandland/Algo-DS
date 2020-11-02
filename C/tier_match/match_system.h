#ifndef MATCH_SYSTEM_H
#define MATCH_SYSTEM_H

#include <stdlib.h>
#include "tier_system.h"

typedef struct {
    TierSystem* stone;
    TierSystem* bronze;
    TierSystem* silver;
    TierSystem* gold;
    TierSystem* uranium;
    TierSystem* vibranium;
} MatchSystem;

MatchSystem* make_match_system();

void delete_match_system(MatchSystem* ms);

void join_match(MatchSystem* ms, char* user_id, Tier tier, Pos pos);

void print_rem_all(MatchSystem* ms);

#endif
