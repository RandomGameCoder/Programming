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

term* Multiply(term* head1, term* head2) {
    term* ptr1 = head1->next, *ptr2, *ptr3, *temp;
    term* head3 = (term*) malloc(sizeof(term));
    head3->coeff = NULL;
    head3->exp = NULL;
    head3->next = NULL;
    while (ptr1!=NULL) {
        ptr2 = head2->next;
        while (ptr2!=NULL) {
            temp = (term*) malloc(sizeof(term));
            temp->coeff = ptr1->coeff * ptr2->coeff;
            temp->exp = ptr1->exp + ptr2->exp;
            ptr3 = head3;
            while(ptr3->next!=NULL && ptr3->next->exp>temp->exp) {
                ptr3 = ptr3->next;
            }
            if(ptr3->next == NULL) {
                temp->next = NULL;
                ptr3->next = temp;
            }
            else if(ptr3->next->exp == temp->exp) {
                ptr3->next->coeff += temp->coeff;
                free(temp);
            }
            else {
                temp->next = ptr3->next;
                ptr3->next = temp;
            }
            ptr2 = ptr2->next;
        }
        ptr1 = ptr1->next;
    }
    return head3;
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

    head3 = Multiply(head1,head2);
    
    ShowPoly(head3);
}
