#include <stdio.h>

int main()
{
    char a;
    char *p = &a;
    printf("%p\n%p", p, &a);
    return 0;
}
