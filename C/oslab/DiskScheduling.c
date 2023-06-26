#include<stdio.h>
#include<stdlib.h>

void Seqandtime(int n, int seq[], int head) {
    int seek = 0, curr = head;
    printf("\nThe seek sequence is : %d ", head);
    for(int i = 0; i < n; i++) {
        printf("-> %d ", seq[i]);
        seek += abs(curr-seq[i]);
        curr = seq[i];
    }
    printf("\n\nSeek time : %d\n", seek);
}

void main() {
    int max = 99, n, seq[20], head, prev, op, f = 0, dir = 1, i, temp, index;
    while(f == 0) {
        printf("1: Change limit (current : %d)\n2: Input head pointer\n3: Seek sequence\n", max);
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
            if(prev-head < 0)
                dir = -1;
            break;
        case 3:
            printf("Enter the number of locations to seek: ");
            scanf("%d", &n);
            printf("Enter the seek sequence: ");
            for(i = 0; i < n; i++) {
                scanf("%d", &seq[i]);
            }
            printf(" \nFCFS\n");
            Seqandtime(n, seq, head);
            i = head;
            index = 0;
            while(!(i == max || i == 0)) {
                for(int j = index; j < n; j++) {
                    if(seq[j]==i) {
                        temp = seq[index];
                        seq[index] = seq[j];
                        seq[j] = temp;
                        index++;
                    }
                }
                i+=dir;
            }
            seq[n] = seq[index];
            seq[index] = i;
            index++;
            n++;
            seq[n] = max-i;
            dir *= -1;
            i = head;
            while(index < n) {
                for(int j = index; j < n; j++) {
                    if(seq[j]==i) {
                        temp = seq[index];
                        seq[index] = seq[j];
                        seq[j] = temp;
                        index++;
                    }
                }
                i+=dir;
            }
            printf(" \nSCAN\n");
            Seqandtime(n, seq, head);
            dir *= -1;
            n++;
            i = head;
            index = 0;
            while(index < n) {
                for(int j = index; j < n; j++) {
                    if(seq[j]==i) {
                        temp = seq[index];
                        seq[index] = seq[j];
                        seq[j] = temp;
                        index++;
                    }
                }
                i=(i+dir)%(max+1);
            }
            printf(" \nC SCAN\n");
            Seqandtime(n, seq, head);
            break;
        default:
            break;
        }
    }
}
