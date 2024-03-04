//gcc -m32 -g goodbye_passwd.c -o goodbye_passwd -fno-stack-protector -no-pie -z execstack

#include <stdio.h>
#include <string.h>

#include "cfg.h"               /* valid password is here */

#define MAX_PASS_LEN 10

/* returns 1 if the given password matches the allowed password. 
   Otherwise returns 0 */
int IsValidPasswd(char* passwd)
{
   int result = 0;
   char buffer_passwd[MAX_PASS_LEN];

   strcpy(buffer_passwd, passwd); 
 
   /* Is the given password the same as the valid password? */ 
   if(!strcmp(buffer_passwd, VALID_PASSWD))
   {
      result = 1; /* yes, valid */
   }
   
   printf("[After] buffer is %s\n", buffer_passwd);
   return result;
}


int main(int argc, char *argv[]) {

   int status = IsValidPasswd(argv[1]);

   printf("Passwd status is: %d\n", status);

   if(status)
   {
      printf("Access Granted!\n");
   }
   else
   {
      printf("Access Denied!\n");
   }

   return 0;
}


