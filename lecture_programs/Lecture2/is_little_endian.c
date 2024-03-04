#include <stdio.h>

int is_little_endian(void) {

  int x = 1;
 
  char byte = *(char *) &x;
  
  return byte;
}

int main()
{
  printf("is_little_endian:%d\n", is_little_endian());

  return 0;
}
