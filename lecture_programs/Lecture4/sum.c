// Program to demonstrate cpu flag operations
// intmax = 2147483647

#include <stdio.h>

int sum(int x, int y)
{
  int t = x + y;
  return t;
}

int main()
{
  int x,y;  
  printf("Enter x int:");
  scanf("%d", &x);

  printf("Enter y int:");
  scanf("%d", &y);
  return sum(x, y);
}
