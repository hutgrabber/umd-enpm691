/* Program to demonstrate arithmetic  right shift */

#include <stdio.h>

int mull12(int x)
{
    return 12*x;
}

int main()
{
  int a;

  printf("Enter one int:");
  scanf("%d", &a);
  printf("Result is:%d\n", mull12(a));

  return 0;
}
