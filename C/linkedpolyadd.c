#include <stdio.h>
#include <stdlib.h>

typedef struct term {
    int coeff, exp;
    struct term* next;
} term;

term* CreatePoly() {
    int a,b,n;
    term *head = (term*) malloc(sizeof(term)),*temp, *ptr;
    head->coeff = NULL;
    head->exp = NULL;
    head->next = NULL;
    printf("Enter the no. of terms in the polynomial: ");
    scanf("%d", &n);
    for(int i = 0; i<n; i++) {
        temp = (term*) malloc(sizeof(term));
        printf("Enter the coeffitient: ");
        scanf("%d",&a);
        printf("Enter the exponent: ");
        scanf("%d",&b);
        temp->coeff = a;
        temp->exp = b;
        ptr = head;
        while (ptr->next!=NULL && ptr->next->exp>temp->exp) {
            ptr = ptr->next;
        }
        if(ptr->next == NULL) {
            temp->next = NULL;
            ptr->next = temp;
        }
        else {
            temp->next = ptr->next;
            ptr->next = temp;
        }
    }
    return head;
}

void ShowPoly(term* head) {
    term* ptr = head->next;
    while (ptr->next!=NULL) {
        printf("%dx^%d + ",ptr->coeff,ptr->exp);
        ptr = ptr->next;
    }
    printf("%dx^%d\n",ptr->coeff,ptr->exp);
}

term* Add(term* head1, term* head2) {
    term *ptr1, *ptr2, *head, *ptr3;
    ptr1 = head1->next;
    ptr2 = head2->next;
    head = (term*) malloc(sizeof(term));
    head->next = NULL;
    ptr3 = head;
    while(ptr1 != NULL && ptr2 != NULL) {
        ptr3->next = (term*) malloc(sizeof(term));
        ptr3 = ptr3->next;
        ptr3->next = NULL;
        if(ptr1->exp == ptr2->exp) {
            ptr3->exp = ptr1->exp;
            ptr3->coeff = ptr1->coeff + ptr2->coeff;
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        else if(ptr1->exp > ptr2->exp) {
            ptr3->exp = ptr1->exp;
            ptr3->coeff = ptr1->coeff;
            ptr1 = ptr1->next;
        }
        else {
            ptr3->exp = ptr2->exp;
            ptr3->coeff = ptr2->coeff;
            ptr2 = ptr2->next;
        }
    }
    while(ptr1 != NULL) {
        ptr3->next = (term*) malloc(sizeof(term));
        ptr3 = ptr3->next;
        ptr3->next = NULL;
        ptr3->exp = ptr1->exp;
        ptr3->coeff = ptr1->coeff;
        ptr1 = ptr1->next;
    }
    while(ptr2 != NULL) {
        ptr3->next = (term*) malloc(sizeof(term));
        ptr3 = ptr3->next;
        ptr3->next = NULL;
        ptr3->exp = ptr2->exp;
        ptr3->coeff = ptr2->coeff;
        ptr2 = ptr2->next;
    }
    return head;
}

void main() {
    term *head1, *head2, *head3;
    int op;

    printf("Enter the first polynomial:\n");
    head1 = CreatePoly();
    printf("Enter the second polynomial:\n");
    head2 = CreatePoly();

    printf("Enter the operation(1.Addition,2.Multiplication): ");
    scanf("%d", &op);

    ShowPoly(head1);
    ShowPoly(head2);

    head3 = Add(head1,head2);
    
    ShowPoly(head3);
}
