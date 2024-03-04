// Program to demonstrate loops
// Change the function in main() to observe
// different behaviors
// gbd: run < <((python3 -c "print('6');"))
#include <stdio.h>
#define WSIZE 8*sizeof(int)

int pcount_do(unsigned x) {
  int result = 0;
  do {
    result += x & 0x1;
    x >>= 1;
  } while (x);
  return result;
}

int pcount_while(unsigned x) {
  int result = 0;
  while (x) {
    result += x & 0x1;
    x >>= 1;
  }
  return result;
}

int pcount_for(unsigned x) {
  int i;
  int result = 0;
  for (i = 0; i < WSIZE; i++) {
    unsigned mask = 1 << i;
    result += (x & mask) != 0;
  }
  return result;
}


int main()
{
    unsigned x;  
    printf("Enter x uint:");
    scanf("%d", &x);
    printf("Ones:%d\n",pcount_while(x));
    return 0;
}

