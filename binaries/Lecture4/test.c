// Program to demonstrate cpu flag operations
// gbd: run < <((python3 -c "print('0'); print('0');"))
#include <stdio.h>

int test(int x, int y) { 
   if(x & y)  return 1;
   else return 0; 
}


int main()
{
  int x,y;  
  printf("Enter x int:");
  scanf("%d", &x);

  printf("Enter y int:");
  scanf("%d", &y);
  return test(x, y);
}
