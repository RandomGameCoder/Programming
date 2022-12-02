#include <stdio.h>

typedef struct sp{
    int row, col, val;
} term;

void main() {
    int m, n, temp, k=1;
    term a[20],b[20];

    printf("Enter the dimensions of the matrix:");
    scanf("%d%d", &m,&n);

    a[0].col = n;
    a[0].row = m;
    b[0].row = n;
    b[0].col = m;

    printf("Enter the matrix elements: \n");
    for (int i = 0; i < a[0].row; i++) {
        for (int j = 0; j < a[0].col; j++) {
            scanf("%d", &temp);
            if(temp!=0) {
                a[k].row = i;
                a[k].col = j;
                a[k].val = temp;
                k++;
            }
        }
    }
    a[0].val = k-1;

    k =1;
    for(int i = 0; i<a[0].col; i++) {
        for(int j = 1; j<a[0].val+1; j++) {
            if(a[j].col == i) {
                b[k].row = a[j].col;
                b[k].col = a[j].row;
                b[k].val = a[j].val;
                k++;
            }
        }
    }
    b[0].val = k-1;

    printf("The transpose of the given matrix is: \n");
    k = 1;
    for (int i = 0; i < b[0].row; i++) {
        for (int j = 0; j < b[0].col; j++) {
            if(b[k].row == i && b[k].col == j) {
                printf("%d ",b[k].val);
                k++;
            }
            else {
                printf("0 ");
            }
        }
        printf("\n");
    }
    
}