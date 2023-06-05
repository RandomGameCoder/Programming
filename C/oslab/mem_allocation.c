#include<stdio.h>
#include<stdlib.h>

typedef struct partition {
    int size, total;
    struct partition *next;
} partition;

partition *PARTS = NULL;

void showPartitions() {
    partition *ptr = PARTS;
    if(ptr == NULL)
        printf("No Partitions Available.");
    else {
        printf("Partitions:\n");
        while(ptr!=NULL) {
            printf("%d KB\n", ptr->size);
            ptr = ptr->next;
        }
    }
}

void clear() {
    partition *ptr = PARTS;
    while(ptr!=NULL) {
        ptr->size = ptr->total;
        ptr = ptr->next;
    }
    showPartitions();
}

int FirstFit(int size) {
    partition *ptr = PARTS;
    if(ptr == NULL)
        return -1;
    else {
        while(ptr!=NULL && ptr->size<size)
            ptr = ptr->next;
        if(ptr == NULL)
            return 0;
        else {
            ptr->size-=size;
            return ptr->size+size;
        }
    }
}

int WorstFit(int size) {
    partition *ptr = PARTS, *max = NULL;
    if(ptr == NULL)
        return -1;
    else {
        while(ptr!=NULL) {
            if(ptr->size>size) {
                if(max == NULL || ptr->size>max->size)
                    max = ptr;
            }
            ptr = ptr->next;
        }
        if(max == NULL)
            return 0;
        else {
            max->size-=size;
            return max->size+size;
        }
    }
}

int BestFit(int size) {
    partition *ptr = PARTS, *best = NULL;
    if(ptr == NULL)
        return -1;
    else {
        while(ptr!=NULL) {
            if(ptr->size>size) {
                if(best == NULL || ptr->size<best->size)
                    best = ptr;
            }
            ptr = ptr->next;
        }
        if(best == NULL)
            return 0;
        else {
            best->size-=size;
            return best->size+size;
        }
    }
}

void main() {
    int f = 0, op, size;
    while(f == 0) {
        printf("\nEnter the operation to perform\n");
        printf("1: Add Partition\n2: First fit\n3: Worst fit\n4: Best fit\n5: Clear Partitions\n6: exit\n::");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            partition *p = (partition*) malloc(sizeof(partition)), *ptr;
            p->next = NULL;
            printf("\nEnter the size of the partition(in KB): ");
            scanf("%d", &size);
            p->size = size;
            p->total = size;
            if(PARTS == NULL)
                PARTS = p;
            else {
                ptr = PARTS;
                while(ptr->next!=NULL)
                    ptr = ptr->next;
                ptr->next = p;
            }
            showPartitions();
            break;
        case 2:
            printf("\nEnter the size of process to be allocated(in KB): ");
            scanf("%d", &size);
            size = FirstFit(size);
            if(size == 0)
                printf("No Partition avalable to fit the given process!!\n");
            else if(size == -1)
                printf("No Partitions available!!\n");
            else
                printf("The process allocated to memory partition with %d KB size\n", size);
            showPartitions();
            break;
        case 3:
            printf("\nEnter the size of process to be allocated(in KB): ");
            scanf("%d", &size);
            size = WorstFit(size);
            if(size == 0)
                printf("No Partition avalable to fit the given process!!\n");
            else if(size == -1)
                printf("No Partitions available!!\n");
            else
                printf("The process allocated to memory partition with %d KB size\n", size);
            showPartitions();
            break;
        case 4:
            printf("\nEnter the size of process to be allocated(in KB): ");
            scanf("%d", &size);
            size = BestFit(size);
            if(size == 0)
                printf("No Partition avalable to fit the given process!!\n");
            else if(size == -1)
                printf("No Partitions available!!\n");
            else
                printf("The process allocated to memory partition with %d KB size\n", size);
            showPartitions();
            break;
        case 5:
            clear();
            break;
        case 6:
            printf("\nExiting...");
            f=1;
            break;
        default:
            printf("\nInvalid option\n");
            break;
        }
    }
}