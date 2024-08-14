#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} node;

void display(node* ptr) {
    while(ptr!=NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
}

node* inbegin(node* ptr, int val) {
    node* temp = (node*) malloc(sizeof(node));
    temp->data = val;
    if(ptr == NULL)
        temp->next = NULL;
    else
        temp->next = ptr;
    ptr = temp;
    return ptr;
}

void inend(node* ptr, int val) {
    node* temp = (node*) malloc(sizeof(node));
    temp->data = val;
    temp->next = NULL;
    while(ptr->next!=NULL) {
        ptr = ptr->next;
    }
    ptr->next = temp;
}

void insert(node* ptr, int val, int pos) {
    int i = 0;
    while(ptr!= NULL && i!=pos) {
        ptr = ptr->next;
        i++;
    }
    if(ptr == NULL) {
        printf("The list is not having the given index..");
    }
    else {
        node* temp = (node*) malloc(sizeof(node));
        temp->data = val;
        temp->next = ptr->next;
        ptr->next = temp;
    }
}

node* delbegin(node* ptr) {
    node* temp = ptr;
    ptr = ptr->next;
    free(temp);
    return ptr;
}

void delend(node* ptr) {
    node* temp;
    while(ptr->next->next != NULL) {
        ptr = ptr->next;
    }
    temp = ptr->next;
    ptr->next = NULL;
    free(temp);
}

void delete(node* ptr, int pos) {
    node* temp;
    int i = 0;
    while(ptr!= NULL && i!=pos) {
        ptr = ptr->next;
        i++;
    }
    if(ptr == NULL) {
        printf("The list is not having the given index..");
    }
    else {
        temp = ptr->next;
        ptr->next = ptr->next->next;
        free(temp);
    }
}

void main() {
    node* head = NULL;
    int f = 0, op = 0, val, pos;
    while(f == 0) {
        printf("\n1.Display\n2.Insert at begining\n3.Insert at end\n4.Insert at specific position");
        printf("\n5.Delete from begining\n6.Delete from end\n7.Delete from specific position\n8.Quit\n");
        printf("Enter the operation to be done: ");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            display(head);
            break;
        
        case 2:
            printf("Enter the value to be inserted: ");
            scanf("%d", &val);
            head = inbegin(head,val);
            break;

        case 3:
            printf("Enter the value to be inserted: ");
            scanf("%d", &val);
            if (head == NULL){
                head = inbegin(head, val);
            }
            else {
                inend(head, val);
            }
            break;
        
        case 4:
            printf("Enter the value to be inserted: ");
            scanf("%d", &val);
            printf("Enter the index to be inserted in: ");
            scanf("%d", &pos);
            insert(head,val,pos);
            break;

        case 5:
            if(head!=NULL)
                head = delbegin(head);
            else
                printf(".....List Empty.....");
            break;
        
        case 6:
            if(head==NULL)
                printf(".....List Empty.....");
            else if(head->next == NULL)
                head = delbegin(head);
            else
                delend(head);
            break;
        
        case 7:
            if(head==NULL)
                printf(".....List Empty.....");
            else
                printf("Enter the index to be inserted in: ");
                scanf("%d", &pos);
                delete(head,pos);
            break;

        case 8:
            f = 1;
            break;
        
        default:
            printf("Invalid option");
            break;
        }
    }
}