// gcc -m32 fPointer.c -o fPointer -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -z execstack


#include <stdio.h>
#include <string.h>

void badFunction(char* str) {       
   printf("%s\n", str);       
   system("any command");
}
int main(int argc, char** argv) 
{   
     void (*ptr)(char* str);  
     ptr = &badFunction;    
     char buff[64];   
     strcpy(buff, argv[1]);    
    (*ptr)(argv[2]);
}

