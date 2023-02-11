
#include <stdio.h>

int items[5], front = -1, rear = -1, SIZE=5;

int isFull()
{
    if ((front == rear + 1) || (front == 0 && rear == SIZE - 1)) 
    {
        return 1;
    }
    return 0;
}

int isEmpty()
{
    if (front == -1)
    {
        return 1;
    }
    return 0;
}

void EnQueue(int value)
{
    if (isFull())
    {
        printf("Queue is Full\n");
    }
    else 
    {
        if (front == -1)
        {
            front = 0;
        }
        rear = (rear+1) % SIZE;
        items[rear] = value;
        printf("Inserted : %d\n", value);
    }
}

void DeQueue()
{
    int element;
    if (isEmpty())
    {
        printf("Queue is Empty\n");
    }
    else 
    {
        element = items[front];
        if (front == rear)
        {
            front = -1;
            rear = -1;
        }
        else
        {
            front = (front+1) % SIZE;
        }
        printf("Deleted : %d\n", element);
    }
}

void display()
{
    if (isEmpty())
    {
        printf("Queue is Empty\n");
    }
    else 
    {
        int i;
        printf("Queue elements are:\n");
        for (i = front; i != rear; i = (i+1) % SIZE)
        {
            printf("%d  ", items[i]);
        }
        printf("%d  ", items[i]);
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
