#ifndef ENUMS_H
#define ENUMS_H

typedef enum { top, mid, bottom, side } Pos;
typedef enum { stone, bronze, silver, gold, uranium, vibranium } Tier;

char* str_pos(Pos pos);

char* str_tier(Tier tier);

#endif
