
#include <stdio.h>

int items[50], front = -1, rear = -1, SIZE=50;

void EnQueue(int value)
{
    if (rear == SIZE - 1)
    {
        printf("Queue is Full\n");
    }
    else 
    {
        if (front == -1)
        {
            front = 0;
        }
        rear++;
        items[rear] = value;
        printf("Inserted : %d\n", value);
    }
}

void DeQueue()
{
    if (front == -1)
    {
        printf("Queue is Empty\n");
    }
    else 
    {
        printf("Deleted : %d\n", items[front]);
        front++;
        if (front > rear)
        {
            front = -1;
            rear = -1;
        }
    }
}

void display()
{
    if (rear == -1)
    {
        printf("Queue is Empty\n");
    }
    else 
    {
        int i;
        printf("Queue elements are:\n");
        for (i = front; i <= rear; i++)
        {
            printf("%d  ", items[i]);
        }
    }
    printf("\n");
}


int main()
{
    int op, value,x=1;
    while (x)
    {
        printf("1. Enqueue\n2. DeQueue\n3. Display\n4. Exit\n");
        printf("\nEnter Operation: ");
        scanf("%d", &op);
        printf("\n");
        switch (op)
        {
            case 1:
            {
                printf("Enter the value to insert: ");
                scanf("%d", &value);
                EnQueue(value);
                printf("\n\n");
                break;
            }
            
            case 2:
            {
                DeQueue();
                printf("\n");
                break;
            }
            
            case 3:
            {
                display();
                printf("\n");
                break;
            }
            
            case 4:
            {
                x=0;
                break;
            }
            default:
            {
                printf("Invalid Input\n");
                printf("\n");
            }
        }
    }
    printf("Program Terminated\n");
}
