//gcc system64.c -o system64 -fno-stack-protector -no-pie -mpreferred-stack-boundary=4 -fno-pic

#include<stdlib.h>

void main()
{
    system("/bin/sh");
}
