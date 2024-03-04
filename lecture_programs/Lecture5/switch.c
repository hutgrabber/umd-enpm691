// Program to demonstrate cpu flag operations
// gbd: run < <((python3 -c "print('0'); print('0');"))
#include <stdio.h>


long switch_eg(long x, long y, long z)
{
    long w = 1;
    switch (x) {
        case 1:
            w = y*z;
            break;
        case 2: 
            w = y/z;
            // fall through
        case 3:
            w += z;
            break;
        case 5:
        case 6:
            w -= z;
            break;
        default:
            w = 2;
    }
    return w;
}


int main()
{
  long x,y,z;  
  printf("Enter x long:");
  scanf("%d", &x);

  printf("Enter y long:");
  scanf("%d", &y);

  printf("Enter z long:");
  scanf("%d", &z);



  return switch_eg(x, y, z);
}
