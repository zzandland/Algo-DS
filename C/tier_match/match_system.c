#include <stdbool.h>
#include <stdio.h>
#include "enums.h"
#include "match_system.h"
#include "node.h"
#include "tier_system.h"

MatchSystem* make_match_system() {
    MatchSystem* ms = (MatchSystem*) malloc(sizeof(MatchSystem));
    ms->stone = make_tier_system(stone);
    ms->bronze = make_tier_system(bronze);
    ms->silver = make_tier_system(silver);
    ms->gold = make_tier_system(gold);
    ms->uranium = make_tier_system(uranium);
    ms->vibranium = make_tier_system(vibranium);
    return ms;
}

void delete_match_system(MatchSystem* ms) {
    print_rem_all(ms);
    printf("\n");
    delete_tier_system(ms->stone);
    delete_tier_system(ms->bronze);
    delete_tier_system(ms->silver);
    delete_tier_system(ms->gold);
    delete_tier_system(ms->uranium);
    delete_tier_system(ms->vibranium);
    free(ms);
}

void join_match(MatchSystem* ms, char* user_id, Tier tier, Pos pos) {
    Node* player = make_node(user_id, tier, pos);

    switch (tier) {
        case stone:
            enqueue_pos(ms->stone, player);
            if (is_match_ready(ms->stone)) start_match(ms->stone);
            break;
        case bronze:
            enqueue_pos(ms->bronze, player);
            if (is_match_ready(ms->bronze)) start_match(ms->bronze);
            break;
        case silver:
            enqueue_pos(ms->silver, player);
            if (is_match_ready(ms->silver)) start_match(ms->silver);
            break;
        case gold:
            enqueue_pos(ms->gold, player);
            if (is_match_ready(ms->gold)) start_match(ms->gold);
            break;
        case uranium:
            enqueue_pos(ms->uranium, player);
            if (is_match_ready(ms->uranium)) start_match(ms->uranium);
            break;
        case vibranium:
            enqueue_pos(ms->vibranium, player);
            if (is_match_ready(ms->vibranium)) start_match(ms->vibranium);
            break;
    }
}

void print_rem_all(MatchSystem* ms) {
    print_rem_tier_system(ms->stone);
    print_rem_tier_system(ms->bronze);
    print_rem_tier_system(ms->silver);
    print_rem_tier_system(ms->gold);
    print_rem_tier_system(ms->uranium);
    print_rem_tier_system(ms->vibranium);
}
