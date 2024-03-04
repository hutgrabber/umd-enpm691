//gcc -m32 -g deadCode.c -o deadCode -fno-stack-protector -no-pie -mpreferred-stack-boundary=2

#include <unistd.h>
#include<stdio.h>
 
void deadCode()
{
   printf("I’m alive!");
   exit(0);
}

void getData()
{
        char buffer[4];
        gets(buffer);
        puts(buffer);
}


int main(int argc, char *argv[ ])
{
   getData();
   return 0;
}

