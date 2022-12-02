#include <stdio.h>
#include <stdlib.h>

union val {
    int a;
    char b;
};

typedef struct node {
    int type;
    union val item;
} node;

void main() {}