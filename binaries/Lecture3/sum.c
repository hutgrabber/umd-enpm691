/* Program to demonstrate arithmetic  right shift */

#include <stdio.h>

int mull12(int x)
{
    return 12*x;
}

int sum(int x, int y)
{
  int t = x+y;
  return t;
}

int main()
{
  int a;
  int b;

  printf("Enter one int:");
  scanf("%d", &a);
  printf("Enter one int:");
  scanf("%d", &b);

  printf("Result is:%d\n", sum(a,b));

  return 0;
}
