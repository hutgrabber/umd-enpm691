/* Program to demonstrate arithmetic  right shift */

#include <stdio.h>

void swap(int *xp, int *yp) 
{
  int t0 = *xp;
  int t1 = *yp;
  *xp = t1;
  *yp = t0;
}


int main()
{
  int a;
  int b;

  printf("Enter one int:");
  scanf("%d", &a);
  printf("Enter one int:");
  scanf("%d", &b);

  swap( &a, &b);

  return 0;
}
