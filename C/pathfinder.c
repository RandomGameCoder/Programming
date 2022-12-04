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

void clear(node *a) {
    node* temp;
    while(a != NULL) {
        temp = a;
        a = a->next;
        free(temp);
    }
}

//0. north
//1. south
//2. east
//3. west
//4. northeast
//5. northwest
//6. southeast
//7. southwest

//recursive function to search the path
ret* search(int** arr, int m, int n, int a, int b, node* head) {
    ret *retvals[8], *cur;
    node *ptr = head, *temp;
    int min = -1;
    if(a == m-1 && b == n-1) {
        cur = (ret*) malloc(sizeof(ret));
        temp = (node*) malloc(sizeof(node));
        temp->r = a;
        temp->c = b;
        temp->next = NULL;
        cur->len = 1;
        cur->start = temp;
        return cur;
    }
    else {
        //initialising list to null
        for(int i = 0; i<8; i++) {
            retvals[i] = NULL;
        }

        //add current position to head
        while(ptr->next != NULL) { 
            ptr = ptr->next;
        }
        ptr->next = (node*) malloc(sizeof(node));
        ptr = ptr->next;
        ptr->r = a;
        ptr->c = b;
        ptr->next = NULL;

        //search in each direction

        //remove current position from head

        //find shortest from all returned paths

        //if all path null, return null

        //if shortest path found, return length and list after inserting
        //current position in list
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