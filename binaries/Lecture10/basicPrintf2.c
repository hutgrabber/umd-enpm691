//gcc -m32 basicPrintf2.c -o basicPrintf2 -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic 

#include <stdio.h>

int main()
{
    int i = -1;
    printf("%20u\n",i);
    printf("%20x\n",i);
    printf("%20d\n",i);
    printf("%20c\n",i);

    return 0;
}

