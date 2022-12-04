#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int r, c;
    struct node* next;
} node;

typedef struct retval {
    int len;
    node *start;
} ret;

void clear(ret *a) {}

ret* search(int** arr, int m, int n, int a, int b, int dir) {
    ret *a[8], *cur;
    int min = -1;
    if(a-1!=0 && arr[a-1][b]!=1 && dir!=1) //north
        a[0]=search(arr, m, n, a-1, b, 2);
    if(a+1!=m && arr[a+1][b]!=1 && dir!=2) //south
        a[1]=search(arr, m, n, a+1, b, 1);
    if(b+1!=n && arr[a][b+1]!=1 && dir!=3) //east
        a[2]=search(arr, m, n, a, b+1, 4);
    if(b-1!=0 && arr[a][b-1]!=1 && dir!=4) //west
        a[3]=search(arr, m, n, a, b-1, 3);

    //need to change
    if(a-1!=0 && b+1!=n && arr[a-1][b+1]!=1 && dir!=5) //northeast
        a[4]=search(arr, m, n, a-1, b, 2);
    if(a-1!=0 && b-1!=0 && arr[a-1][b-1]!=1 && dir!=6) //northwest
        a[5]=search(arr, m, n, a-1, b, 2);
    if(a+1!=m && b-1!=0 && arr[a+1][b-1]!=1 && dir!=7) //southwest
        a[6]=search(arr, m, n, a-1, b, 2);
    if(a+1!=m && b+1!=n && arr[a+1][b+1]!=1 && dir!=8) //southeast
        a[7]=search(arr, m, n, a-1, b, 2);
    for(int i = 0; i<8; i++) {
        if(i == dir) {
            clear(a[i])
            continue;
        }
        if(a[i]!= NULL && (min == -1 || a[min]->len>a[i]->len)) {
            min = i;
        }
    }
}

void main() {
    int arr[6][6] = {
        {0,0,1,0,1,0},
        {0,1,0,0,1,0},
        {1,1,0,1,0,0},
        {1,0,0,1,1,1},
        {0,0,1,0,1,0},
        {0,0,1,0,0,0}
    }
}