#include<stdio.h>

void main() {
    int r, p, f, index = 0, n;
    int allocation[10][10], max[10][10], available[10], need[10][10], finish[10], safe[10];
    printf("Enter the number of resources: ");
    scanf("%d", &r);
    printf("\nEnter the number of processes: ");
    scanf("%d", &p);
    printf("\nEnter the matrices...\n");
    for(int i = 0; i < p; i++) {
        printf("\nEnter the Max resources needed for process %d...", i+1);
        for (int j = 0; j < r; j++) {
            printf("\n\tNumber of instances of resource %d: ", j+1);
            scanf("%d", &max[i][j]);
        }
        printf("\nEnter the Allocated resources of process %d...", i+1);
        for (int j = 0; j < r; j++) {
            printf("\n\tNumber of instances of resource %d: ", j+1);
            scanf("%d", &allocation[i][j]);
            need[i][j] = max[i][j] - allocation[i][j];
        }
        finish[i] = 0;
    }
    printf("\nEnter the available instances of each resource...\n");
    for (int i = 0; i < r; i++) {
        printf("Number of instances of resource %d: ", i+1);
        scanf("%d", &available[i]);
    }

    printf("\nThe need matrix is :\n");
    for(int i = 0; i<p; i++) {
        for(int j = 0; j<r; j++) {
            printf("%d ", need[i][j]);
        }
        printf("\n");
    }

    f = 0;
    for(int i = 0; i < p; i++) {
        n = 1;
        for(int j = 0; j < r; j++) {
            if(need[i][j] > available[j])
                n = 0;
        }
        if(finish[i] != 1 && n == 1) {
            f = 1;
            finish[i] = 1;
            for (int j = 0; j < r; j++) {
                available[j] += allocation[i][j];
                allocation[i][j] = 0;
            }
            safe[index] = i;
            index++;
        }
        if(i == p-1) {
            n = 1;
            for(int j = 0; j < p; j++) {
                if(finish[j] == 0)
                    n = 0;
            }
            if(f == 0 || n == 1)
                break;
            else
                i = -1;
        }
    }
    if(f == 0) {
        printf("The system will encounter a deadlock\n");
    }
    else {
        printf("\n\nSafe State exists in the order <");
        for(int i = 0; i<p; i++) {
            printf(" p%d,", safe[i]);
        }
        printf(" >\n");
    }

}