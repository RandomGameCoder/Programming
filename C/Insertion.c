#include <stdio.h>

void main() {
    int n, a[10], i, j, temp;
    
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    printf("Enter the array elements: ");
    for (int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    
    for (i = 1; i < n; i++) {
        j = i - 1;
        temp = a[i];
        while(j>=0 && temp<a[j]) {
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = temp;
    }
    
    printf("The sorted array is: ");
    for (int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
}