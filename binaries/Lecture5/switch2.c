// Program to demonstrate cpu flag operations
// gbd: run < <((python3 -c "print('0'); print('0');"))
#include <stdio.h>


long switch_eg(long x, long y, long z)
{
    long w = 1;
    switch (x) {
        case 0: 
            w = 0;
            break;
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
        case 7:
            w = x*y+1;
            break;
        case 8:
            w = x*y*z;
            break;
        case 9:
            w = y + 2;
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
