int comp(const void *a, const void *b) {
    return strcmp((char *) a, (char *) b);
}

char findTheDifference(char * s, char * t){
    qsort(s, strlen(s), sizeof(char), comp);
    qsort(t, strlen(t), sizeof(char), comp);
    int ln = strlen(s) < strlen(t) ? strlen(s) : strlen(t);
    for (int i = 0; i < ln; ++i) {
        if (s[i] != t[i]) return t[i];
    }
    return t[strlen(t)-1];
}