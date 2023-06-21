#include<stdio.h>

void FCFS(int n, int seq[], int head) {
    int seek = 0;
    for(int i = 0; i < n; i++) {
        seek += abs(head-seq[i]);
    }
    printf("Seek time : %d", seek);
}

void main() {
    int max = 99, n, seq[20], head, prev, op, f = 0;
    while(f == 0) {
        printf("1: Change limit (current : %d)\n2: Input head pointer\n3: Seek sequence\n", max)
        printf("\nEnter the option: ");
        scanf("%d", &op);
        switch(op) {
        case 1:
            printf("\nEnter the max limit of disk: ");
            scanf("%d", &max);
            break;
        case 2:
            printf("Enter head pointer: ");
            scanf("%d", &head);
            printf("Enter previous pointer location(same as head if none): ");
            scanf("%d", &prev);
            break;
        case 3:
            printf("Enter the number of locations to seek: ");
            scanf("%d", &n);
            printf("Enter the seek sequence: ");
            for(int i = 0; i < n; i++) {
                scanf("%d", &seq[i]);
            }
            FCFS(n, seq, head);
            break;
        default:
            break;
        }
    }
}