#include<stdio.h>
#include<stdlib.h>

typedef struct use{
    int index;
    struct use *next;
} use;

int MEMORY[10];
int MEM_SIZE = 10;

void ClearMem() {
    for(int i=0; i<MEM_SIZE; i++)
        MEMORY[i] = -1;
}

void FIFO() {
    int hit = 0, page, index = 0, f = 0;
    while(f == 0) {
        hit = 0;
        printf("Enter the page to be accessed(-1 to exit): ");
        scanf("%d", &page);
        if(page<-1) {
            printf("\nInvalid page!\n");
            continue;
        }
        else if(page == -1)
            break;
        for(int i = 0; i<MEM_SIZE; i++) {
            printf("|  %d  ", MEMORY[i]);
            if(MEMORY[i] == page)
                hit = 1;
        }
        if(hit == 1)
            printf("|\nHit.\n");
        else {
            printf("|\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("^\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("|\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("%d\n",page);
            printf("\nMiss.\n");
            MEMORY[index] = page;
            index = (index+1)%MEM_SIZE;
        }
    }
}

void LRU() {
    int hit = 0, page, f = 0;
    use *lru, *mru, *temp;
    for(int i = 0; i<MEM_SIZE; i++) {
        temp = (use*) malloc(sizeof(use));
        temp->next = NULL;
        temp->index = i;
        if(i == 0)
            mru = lru = temp;
        else {
            mru->next = temp;
            mru = temp;
        }
    }
    while(f == 0) {
        hit = 0;
        printf("Enter the page to be accessed(-1 to exit): ");
        scanf("%d", &page);
        if(page<-1) {
            printf("\nInvalid page!\n");
            continue;
        }
        else if(page == -1)
            break;
        for(int i = 0; i<MEM_SIZE; i++) {
            printf("|  %d  ", MEMORY[i]);
            if(MEMORY[i] == page) {
                hit = 1;
                if(lru->index == i) {
                    temp = lru;
                    lru = lru->next;
                    temp->next = NULL;
                    mru->next = temp;
                    mru = mru->next;
                }
                else {
                    temp = lru;
                    while(temp->next->index!=i)
                        temp = temp->next;
                    mru->next = temp->next;
                    mru = mru->next;
                    temp->next = mru->next;
                    mru->next = NULL;
                }
            }
        }
        if(hit == 1)
            printf("|\nHit.\n");
        else {
            printf("|\n   ");
            for(int i=0; i<lru->index; i++)
                printf("      ");
            printf("^\n   ");
            for(int i=0; i<lru->index; i++)
                printf("      ");
            printf("|\n   ");
            for(int i=0; i<lru->index; i++)
                printf("      ");
            printf("%d\n",page);
            printf("\nMiss.\n");
            MEMORY[lru->index] = page;
            temp = lru;
            lru = lru->next;
            temp->next = NULL;
            mru->next = temp;
            mru = mru->next;
        }
    }
}

void LFU() {
    int hit = 0, page, f = 0, usage[MEM_SIZE], index;
    for(int i = 0; i<MEM_SIZE; i++)
        usage[i] = 0;
    while(f == 0) {
        hit = 0;
        printf("Enter the page to be accessed(-1 to exit): ");
        scanf("%d", &page);
        if(page<-1) {
            printf("\nInvalid page!\n");
            continue;
        }
        else if(page == -1)
            break;
        for(int i = 0; i<MEM_SIZE; i++) {
            printf("|  %d  ", MEMORY[i]);
            if(MEMORY[i] == page) {
                hit = 1;
                usage[i]++;
            }
        }
        if(hit == 1)
            printf("|\nHit.\n");
        else {
            index = 0;
            for(int i = 0; i<MEM_SIZE; i++) {
                if(usage[i]<usage[index])
                    index = i;
            }
            printf("|\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("^\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("|\n   ");
            for(int i=0; i<index; i++)
                printf("      ");
            printf("%d\n",page);
            printf("\nMiss.\n");
            MEMORY[index] = page;
            usage[index] = 1;
        }
    }
}

void main() {
    int f = 0, op;
    while(f == 0){
        ClearMem();
        printf("\nEnter the operation to perform:\n");
        printf("1: Change memory size(Current size: %d)\n2: FIFO\n3: LRU\n4: LFU\n5: exit\n::",MEM_SIZE);
        scanf("%d", &op);
        switch(op)
        {
        case 1:
            printf("\nMax memory = 10\n");
            printf("Enter the new size: ");
            scanf("%d", &f);
            if(f<1 || f>10)
                printf("Memory of given size not available!");
            else
                MEM_SIZE = f;
            f = 0;
            break;
        case 2:
            FIFO();
        case 3:
            LRU();
        case 4:
            LFU();
        case 5:
            f = 1;
            break;
        default:
            break;
        }
    }
}