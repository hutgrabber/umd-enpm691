// Program to demonstrate cpu flag operations
// uintmax = 4294967295
// gbd: run < <((python3 -c "print('0'); print('0');"))
#include <stdio.h>

unsigned sum(unsigned x, unsigned y)
{
  int t = x + y;
  return t;
}

int main()
{
  unsigned x,y;  
  printf("Enter x uint:");
  scanf("%d", &x);

  printf("Enter y uint:");
  scanf("%d", &y);
  return sum(x, y);
}
