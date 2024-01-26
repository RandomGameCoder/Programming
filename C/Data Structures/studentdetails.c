#include <stdio.h>
#include <stdlib.h>

typedef struct student {
    int num;
    char name[20];
    float total_marks;
    struct student *next;
} student;

void display(student *ptr) {
    while(ptr!=NULL) {
        printf("%d   %s   %f \n", ptr->num, ptr->name, ptr->total_marks);
        ptr = ptr->next;
    }
}

void insert(student *ptr) {
    int num;
    float marks;
    student *temp = (student*) malloc(sizeof(student)); 
    printf("Enter the number: ");
    scanf("%d",&num);
    printf("Enter name: ");
    scanf("%s", temp->name);
    printf("Enter the total marks: ");
    scanf("%f", &marks);
    temp->num = num;
    temp->total_marks = marks;
    temp->next = NULL;
    while(ptr->next!=NULL) {
        ptr = ptr->next;
    }
    ptr->next = temp;
}

void delete(student *ptr, int num) {
    while(ptr->next!=NULL && ptr->next->num != num) {
        ptr = ptr->next;
    }
    if(ptr->next==NULL) {
        printf("No student with given number was found.");
        return;
    }
    student *temp;
    if(ptr->next->next == NULL) {
        temp = ptr->next;
        ptr->next = temp->next;
        printf("The deleted item:\n");
        printf("%d   %s   %f \n", temp->num, temp->name, temp->total_marks);
        free(temp);
    }
}

void search(student *ptr, int num) {
    while(ptr->next!=NULL && ptr->next->num != num) {
        ptr = ptr->next;
    }
	if(ptr->next == NULL) {
		printf("Student not found");
		return;
	}
	ptr = ptr->next;
	printf("%d   %s   %f \n\n\n", ptr->num, ptr->name, ptr->total_marks);
}

void sort(student *head) {
    student *ptr, *prev, *temp, *start, *min;
    start = head;
    while(start!=NULL) {
        min = start->next;
        ptr = start;
        while(ptr->next!=NULL) {
            if(ptr->next->num<min->num) {
                min = ptr->next;
                prev = ptr;
            }
            ptr = ptr->next;
        }
        if(min!=start->next) {
            temp = min;
            prev->next = temp->next;
            temp->next = start->next;
            start->next = temp;
        }
        start = start->next;
    }
}

void main() {
    student *head = (student*) malloc(sizeof(student));
    head->next = NULL;
    int op, f = 0, num;
    while (f==0) {
        printf("Operator: ");
        scanf("%d", &op);
        switch (op) {
            case 1:
                insert(head);
                break;
            
            case 2:
                printf("Number: ");
                scanf("%d", &num);
                delete(head, num);
                break;
            
            case 3:
                printf("Number: ");
                scanf("%d", &num);
                search(head, num);
                break;

            case 4:
                sort(head);
                break;

            case 5:
                f = 1;
                break;

            default:
                break;
        }
        if(f!=1) {
            display(head->next);
        }
    }
}