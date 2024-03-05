### Context
Given binaries for this homework:
`./hw3`

### Assignment
You must exploit the hw3 binary and get a shell.  

#### Conditions:

ASLR is ON.
Document what version of GLIBC your VM is running. Run "/lib/x86_64-linux-gnu/libc.so.6" in your VM to check; I have version 2.33.
Submission: Provide a zip file with both your python3 POC & a writeup of your exploitation.  This writeup can be in the style of a "Hack the Box Walkthrough", that documents the step-by-step process you took to exploit the code & should include enough detail that someone else could reproduce the exploit from your writeup.  Include relevant discussion on how you beat the various security protections.

Your exploit must work outside of GBD!  If your exploit fails outside of GDB (because you did not defeat ASLR), you will not receive full points.