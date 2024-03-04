//gcc -m32 directPrintfUser.c -o directPrintfUser -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -g 

#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    char b[128];
    strcpy(b, argv[1]); // Ignore buff overflow here.
    printf(b);
    printf("\n");
}

