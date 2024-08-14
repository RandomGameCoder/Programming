#include <stdio.h> 
#include <stdlib.h> 
 
typedef struct node{ 
int data; 
int priority; 
struct node* next; 
} Node; 
 
 
Node* newNode(int d, int p){ 
Node* temp=(Node*)malloc(sizeof(Node)); 
temp->data=d; 
temp->priority=p; 
temp->next=NULL; 
return temp; 
} 
 
 
 
void pop(Node** head){ 
Node* temp=*head; 
(*head)=(*head)->next; 
printf("%d",temp->data); 
free(temp); 
} 
 
void push(Node**head,int d,int p){ 
Node* start=(*head); 
Node* temp=newNode(d, p); 
if((*head)->priority>p){ 
temp->next=*head; 
(*head)=temp; 
} 
else{ 
while(start->next!= NULL && 
start->next->priority < p) { 
start=start->next; 
} 
temp->next=start->next; 
start->next=temp; 
} 
} 
 
void display(Node *Start){ 
Node *temp=Start; 
if(temp==NULL){ 
printf("\nList if empty"); 
return; 
} 
printf("\nThe linked list is"); 
while(temp!=NULL){ 
printf("%d",temp->data); 
temp=temp->next; 
}
} 
 
int isEmpty(Node** head){ 
return (*head)==NULL; 
} 
 
 
int main(){ 
int data,priority; 
printf("Enter first element and priority"); 
scanf("%d%d",&data,&priority); 
Node* pq = newNode(data, priority); 
do{ 
printf("1.Insert 2.Delete 3.Display 4.Exit"); 
printf("Choose your option"); 
scanf("%d",&choice); 
switch(choice){ 
case 1:printf("Enter the value and priority to be inserted"); 
scanf("%d%d",&data,&priority); 
push(&pq,data,priority); 
break; 
case 2:pop(&pq) 
case 3: display(&pq); 
case 4: exit(0); 
default: printf("Invalid Choice"); 
}}while(1); 
 
return 0; 
}
