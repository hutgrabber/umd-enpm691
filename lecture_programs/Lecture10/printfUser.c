//gcc -m32 printfUser.c -o printfUser -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main(int argc, char** argv)
{
    int j = 4;
    int i = 2;
    printf(argv[1]);

    return 0;
}



