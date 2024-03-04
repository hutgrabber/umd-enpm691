#include <stdio.h>

int sum(int x, int y)
{
    int z;
    z = x + y;
    return z;
}


int main()
{
  int a;
  int b;
  int result;
  printf("Enter one int:");
  scanf("%d", &a);
  printf("Enter one int:");
  scanf("%d", &b);

  result = sum(a,b);

  printf("Result is:%d\n", result);

  return 0;
}
