//gcc -m32 basicPrintf3_vuln.c -o basicPrintf3_vuln -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main()
{
    int i = 2;
    printf("%d");

    return 0;
}

