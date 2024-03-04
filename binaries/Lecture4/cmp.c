// Program to demonstrate cpu flag operations
// gbd: run < <((python3 -c "print('0'); print('0');"))
#include <stdio.h>

int max(int x, int y) { 
  if(x <= y)   {     
   return y;   
  }   else   { 
    return x;   
  }
}

int main()
{
  unsigned x,y;  
  printf("Enter x uint:");
  scanf("%d", &x);

  printf("Enter y uint:");
  scanf("%d", &y);
  return max(x, y);
}
