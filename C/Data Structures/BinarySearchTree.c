#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *LC, *RC;
} node;

node* SearchParentIn(int data, node* parent) {
    if(parent->data == data) {return NULL;}
    else if(parent->data > data) {
        if(parent->LC != NULL) 
            SearchParentIn(data, parent->LC);
        else
            return parent;
    }
    else if(parent->data < data) {
        if(parent->RC != NULL) 
            SearchParentIn(data, parent->RC);
        else
            return parent;
    }
}

node* SearchParentOut(int data, node* parent) {
    if(parent->data == data) {return NULL;}
    else if(parent->data > data) {
        if(parent->LC != NULL) {
            if(parent->LC->data != data)
                SearchParentIn(data, parent->LC);
            else
                return parent;
        }
    }
    else if(parent->data < data) {
        if(parent->RC != NULL) {
            if(parent->RC->data != data)
                SearchParentIn(data, parent->RC);
            else
                return parent;
        }
    }
}

node* InsertBST(int data, node* root) {
    node *parent, *new = (node*) malloc(sizeof(node));
    new->LC = NULL;
    new->RC = NULL;
    if(root == NULL) {
        new->data = data;
        return new;
    }
    else {
        parent = SearchParentIn(data, root);
        if(parent == NULL) {
            printf("node already exists");
            free(new);
        }
        else {
            new->data = data;
            if(parent->data >data)
                parent->LC = new;
            else
                parent->RC = new;
        }
        return root;
    }
}

node* DeleteBST(int data, node* root) {
    if(root == NULL)
        printf("Tree Empty");
    else {
        node *parent = SearchParentOut(data, root);
        if(parent == NULL) {
            
        }
    }
}

void BSTTraversal(node* ptr) {
    if(ptr!=NULL) {
        printf("%d \n",ptr->data);
        BSTTraversal(ptr->LC);
        BSTTraversal(ptr->RC);
    }
}

void main() {
    node* root = NULL;
    int op = 0, f = 1, data;
    while (f == 1) {
        printf("Enter the option:");
        scanf("%d", &op);
        switch(op) {
            case 0:
                f = 0;
                break;
            case 1:
                printf("Enter the data:");
                scanf("%d", &data);
                root = InsertBST(data, root);
                break;
            case 2:
                printf("The tree is, \n");
                BSTTraversal(root);
        }
    }
    
}