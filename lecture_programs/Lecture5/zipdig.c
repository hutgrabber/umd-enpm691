#include <stdio.h>

#define ZLEN 5
typedef int zip_dig[ZLEN];



int get_digit(zip_dig z, int dig)
{
  return z[dig];
}


int main()
{
    // declare several arrays
    zip_dig cmu = { 1, 5, 2, 1, 3 };
    zip_dig mit = { 0, 2, 1, 3, 9 };
    zip_dig ucb = { 9, 4, 7, 2, 0 };

    int x;  
    printf("Enter zipdig index: ");
    scanf("%d", &x);
    
    printf("Result is: %d",get_digit(cmu,x));

    return 0;
}
