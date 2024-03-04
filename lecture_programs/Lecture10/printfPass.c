//gcc -m32 printfPass.c -o printfPass -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g

#include <stdio.h>

int main(int argc, char** argv)
{
    char*  userPassword = "This is a user password\n";
    char*  adminPassword = "This is an admin password\n";

    printf(argv[1]);

    return 0;
}



