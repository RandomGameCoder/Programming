#include<stdio.h>
#include<stdlib.h>

typedef struct process{
    int id, priority;
    int arrival, burst, completion;
    int turnaround, waiting;
    struct process *next;
} process;

int NUM_OF_PROCS = 0, TIME_ELAPSED = 0;
process *LIST = NULL;

process* RR(int quanta, process *list, process* complete) {
    process *p = list, *temp = list;
    if(list->next!=NULL) {
        while(temp->next!=NULL) {
            temp = temp->next;
        }
    }
    list = list->next;
    p->next = NULL;
    p->burst -= quanta;
    TIME_ELAPSED += quanta;
    if(p->burst>0) {
        if(temp!=p)
            temp->next = p;
        for(int i=0; i<quanta; i++)
            printf("|   |\n");
    }
    else {
        TIME_ELAPSED += p->burst;
        p->completion = TIME_ELAPSED;
        for(int i=0; i<(quanta+p->burst); i++)
            printf("|   |\n");
        if(complete == NULL)
            complete = p;
        else {
            temp = complete;
            while(temp->next!=NULL){
                temp = temp->next;
            }
            temp->next = p;
        }
    }
    printf("+---+ %d  : p%d\n", TIME_ELAPSED,p->id);
    if(list!=NULL)
        complete = RR(quanta, list, complete);
    return complete;
}

process* SJF_FCFS_Priority(process *list) {
    process *p = list;
    while (p!=NULL) {
        for(int i = 0; i<p->burst; i++)
            printf("|   |\n");
        TIME_ELAPSED += p->burst;
        printf("+---+ %d  : p%d\n", TIME_ELAPSED,p->id);
        p->completion = TIME_ELAPSED;
        p = p->next;
    }
    return list;
}

process* CreateProcess(int arrival, int burst, int priority) {
    process* p = (process*) malloc(sizeof(process));
    p->arrival = arrival;
    p->burst = burst;
    p->completion = -1;
    p->turnaround = -1;
    p->waiting = -1;
    p->next = NULL;
    p->priority = priority;
    return p;
}

void showList(process *list) {
    while(list!=NULL) {
        printf("\nprocess        : %d\n", list->id);
        printf("arrival time   : %d\n", list->arrival);
        printf("burst time     : %d\n", list->burst);
        printf("completion time: %d\n", list->completion);
        printf("priority       : %d\n\n", list->priority);
        list = list->next;
    }
}

process* CopyList() {
    process *list = NULL, *temp = LIST, *p;
    while(temp!=NULL) {
        if(list == NULL) {
            list = CreateProcess(temp->arrival, temp->burst, temp->priority);
            list->id = temp->id;
        }
        else{
            p = list;
            while (p->next!=NULL)
                p = p->next;
            p->next = CreateProcess(temp->arrival, temp->burst, temp->priority);
            p = p->next;
            p->id = temp->id;
        }
        temp = temp->next;
    }
    return list;
}

process* SJFsort(process *list) {
    process *ptr, *temp = NULL, *min, *prev;
    while(list!=NULL) {
        min = list;
        ptr = list;
        while(ptr->next!=NULL) { 
            if(ptr->next->burst<min->burst) {
                prev = ptr;
                min = ptr->next;
            }
            ptr = ptr->next;
        }
        if(min!=list)
            prev->next = min->next;
        else
            list = list->next;
        min->next = NULL;
        if(temp==NULL)
            temp = min;
        else{
            ptr = temp;
            while(ptr->next!=NULL)
                ptr = ptr->next;
            ptr->next = min;
        }
    }
    return temp;
}

process* FCFSsort(process *list) {
    process *ptr, *temp = NULL, *min, *prev;
    while(list!=NULL) {
        min = list;
        ptr = list;
        while(ptr->next!=NULL) { 
            if(ptr->next->arrival<min->arrival) {
                prev = ptr;
                min = ptr->next;
            }
            ptr = ptr->next;
        }
        if(min!=list)
            prev->next = min->next;
        else
            list = list->next;
        min->next = NULL;
        if(temp==NULL)
            temp = min;
        else{
            ptr = temp;
            while(ptr->next!=NULL)
                ptr = ptr->next;
            ptr->next = min;
        }
    }
    return temp;
}

process* Prioritysort(process *list) {
    process *ptr, *temp = NULL, *min, *prev;
    while(list!=NULL) {
        min = list;
        ptr = list;
        while(ptr->next!=NULL) { 
            if(ptr->next->priority<min->priority) {
                prev = ptr;
                min = ptr->next;
            }
            ptr = ptr->next;
        }
        if(min!=list)
            prev->next = min->next;
        else
            list = list->next;
        min->next = NULL;
        if(temp==NULL)
            temp = min;
        else{
            ptr = temp;
            while(ptr->next!=NULL)
                ptr = ptr->next;
            ptr->next = min;
        }
    }
    return temp;
}


void main() {
    int f = 0, op;
    while(f==0) {
        TIME_ELAPSED = 0;
        printf("\nEnter the operation to perform\n1: add process\n2: Round Robin\n3: SJF\n4: FCFS\n5: Priority\n6: exit\n::");
        scanf("%d", &op);
        switch(op) {
            case 1:
                int pr, a, b;
                printf("Enter the arrival time: ");
                scanf("%d", &a);
                printf("Enter the burst time: ");
                scanf("%d", &b);
                printf("Enter the priority(1:High, 2:Normal , 3:Low): ");
                scanf("%d", &pr);
                process* p = CreateProcess(a, b, pr), *temp;
                if(NUM_OF_PROCS == 0)
                    LIST = p; 
                else {
                    temp = LIST;
                    while(temp->next!=NULL)
                        temp = temp->next;
                    temp->next = p;
                }
                NUM_OF_PROCS++;
                p->id = NUM_OF_PROCS;
                printf("\nThe Processes are: \n");
                showList(LIST);
                break;
            case 2:
                if(NUM_OF_PROCS == 0) {
                    printf("No Process in queue.");
                }
                else {
                    process *list = CopyList(), *ptr1, *ptr2;
                    int q;
                    float turnaround = 0, waiting = 0;
                    float avg_turn, avg_wait;

                    list = FCFSsort(list);

                    printf("Enter the time quantum: ");
                    scanf("%d", &q);

                    printf("\nThe Order of executioon is : \n");
                    showList(list);
                    printf("\n\n Gantt chart:");
                    printf("\n\n+---+ %d\n", TIME_ELAPSED);

                    list = RR(q, list, NULL);
                    ptr1 = list;
                    while(ptr1!=NULL) {
                        ptr2 = LIST;
                        while(ptr2->id!=ptr1->id)
                            ptr2 = ptr2->next;
                        ptr1->burst = ptr2->burst;
                        ptr1 = ptr1->next;
                    }

                    ptr1 = list;
                    while(ptr1!=NULL) {
                        ptr1->turnaround = ptr1->completion-ptr1->arrival;
                        ptr1->waiting = ptr1->turnaround-ptr1->burst;
                        turnaround += ptr1->turnaround;
                        waiting += ptr1->waiting;
                        ptr1 = ptr1->next;
                    }

                    avg_turn = turnaround/NUM_OF_PROCS;
                    avg_wait = waiting/NUM_OF_PROCS;

                    printf("\nAverage waiting time = %f\n", avg_wait);
                    printf("\nAverage turnaround time = %f\n", avg_turn);
                }
                break;
            case 3:
                if(NUM_OF_PROCS == 0) {
                    printf("No Process in queue.");
                }
                else {
                    process *list = CopyList(), *ptr1;
                    float turnaround = 0, waiting = 0;
                    float avg_turn, avg_wait;

                    list = SJFsort(list);
                    
                    printf("\nThe Order of executioon is : \n");
                    showList(list);
                    printf("\n\n Gantt chart: \n");
                    printf("\n+---+ %d\n", TIME_ELAPSED);

                    list = SJF_FCFS_Priority(list);

                    ptr1 = list;
                    while(ptr1!=NULL) {
                        ptr1->turnaround = ptr1->completion-ptr1->arrival;
                        ptr1->waiting = ptr1->turnaround-ptr1->burst;
                        turnaround += ptr1->turnaround;
                        waiting += ptr1->waiting;
                        ptr1 = ptr1->next;
                    }

                    avg_turn = turnaround/NUM_OF_PROCS;
                    avg_wait = waiting/NUM_OF_PROCS;

                    printf("\nAverage waiting time = %f\n", avg_wait);
                    printf("\nAverage turnaround time = %f\n", avg_turn);
                }
                break;
            case 4:
                if(NUM_OF_PROCS == 0) {
                    printf("No Process in queue.");
                }
                else {
                    process *list = CopyList(), *ptr1;
                    float turnaround = 0, waiting = 0;
                    float avg_turn, avg_wait;

                    list = FCFSsort(list);

                    printf("\nThe Order of executioon is : \n");
                    showList(list);
                    printf("\n\n Gantt chart:");
                    printf("\n\n+---+ %d\n", TIME_ELAPSED);

                    list = SJF_FCFS_Priority(list);

                    ptr1 = list;
                    while(ptr1!=NULL) {
                        ptr1->turnaround = ptr1->completion-ptr1->arrival;
                        ptr1->waiting = ptr1->turnaround-ptr1->burst;
                        turnaround += ptr1->turnaround;
                        waiting += ptr1->waiting;
                        ptr1 = ptr1->next;
                    }

                    avg_turn = turnaround/NUM_OF_PROCS;
                    avg_wait = waiting/NUM_OF_PROCS;

                    printf("\nAverage waiting time = %f\n", avg_wait);
                    printf("\nAverage turnaround time = %f\n", avg_turn);
                }
                break;
            case 5:
                if(NUM_OF_PROCS == 0) {
                    printf("No Process in queue.");
                }
                else {
                    process *list = CopyList(), *ptr1;
                    float turnaround = 0, waiting = 0;
                    float avg_turn, avg_wait;

                    list = Prioritysort(list);

                    printf("\nThe Order of executioon is : \n");
                    showList(list);
                    printf("\n\n Gantt chart:");
                    printf("\n\n+---+ %d\n", TIME_ELAPSED);

                    list = SJF_FCFS_Priority(list);

                    ptr1 = list;
                    while(ptr1!=NULL) {
                        ptr1->turnaround = ptr1->completion-ptr1->arrival;
                        ptr1->waiting = ptr1->turnaround-ptr1->burst;
                        turnaround += ptr1->turnaround;
                        waiting += ptr1->waiting;
                        ptr1 = ptr1->next;
                    }

                    avg_turn = turnaround/NUM_OF_PROCS;
                    avg_wait = waiting/NUM_OF_PROCS;

                    printf("\nAverage waiting time = %f\n", avg_wait);
                    printf("\nAverage turnaround time = %f\n", avg_turn);
                }
                break;
            case 6:
                f = 1;
                printf("Exiting...");
                break;
            default:
                printf("!!!Invalid option!!!\n");
                break;
        }
    }
}