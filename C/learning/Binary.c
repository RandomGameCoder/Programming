#include <stdio.h>

void main() {
    int n, a[10], key, index = -1; 
    int low = 0, high, mid, temp;
    
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    printf("Enter the array elements: ");
    for (int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < n-i; j++)
        {
            if (a[j]>a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    printf("Enter the key to be found: ");
    scanf("%d", &key);

    high = n-1;
    while(low<=high) {
        mid = (low + high)/2;
        if(a[mid] == key) {
            index = mid;
            break;
        }
        else if(a[mid]>key) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }

    if(index != -1) {
        printf("The key was found.\n");
    }
    else {
        printf("The key was not found.\n");
    }
}