#include <stdio.h>

int prime(int n) {
    int key = 0,i = 2;
    while(i<n/2)
    {
        if(n%i ==0)
            key = 1;
            break;
        i++;
    }
    return key;
    
}
void main()
{
    int n,a;
    printf("Enter a number: ");
    scanf("%d", &n);
    a = prime(n);
    if (a==0)
        printf("The number is prime");
    else
        printf("The number is not prime");
}