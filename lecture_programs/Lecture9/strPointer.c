// gcc -m32 strPointer.c -o strPointer -fno-stack-protector -no-pie -mpreferred-stack-boundary=2 -fno-pic -z execstack


#include <stdio.h>
#include <string.h>

void license(char *arg)
{
  char input[256];  
  char *conf = "test -f ~/.progrc";  
  char *license = "THIS SOFTWARE IS ...";  

  printf(license);  
  strcpy(input, arg);  

  if (system(conf)) 
     printf("Missing . progrc");
}


int main(int argc, char* argv[]){  

    license(argv[1]);
    return 0;
}

