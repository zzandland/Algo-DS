#include "enums.h"

char* str_pos(Pos pos) {
    switch (pos) {
        case top:
            return "상단";
        case mid:
            return "중단";
        case bottom:
            return "하단";
        case side:
            return "옆구리";
    }
}

char* str_tier(Tier tier) {
    switch (tier) {
        case stone:
            return "돌";
        case bronze:
            return "동";
        case silver:
            return "은";
        case gold:
            return "금";
        case uranium:
            return "우라늄";
        case vibranium:
            return "비브라늄";
    }
}
