### Context
Given binaries for this homework:
`./program1` and `./program2`

### Questions
1. For **program 1**, in what function does the buffer overflow occur?
2. For **program 1**, what is the address of the `winner()` function?
3. For **program 1**, How many bytes need to be overwritten before overwriting the return pointer?  Asked another way, how big must your overflow be, not including the return pointer overwrite.?
4. For **program 1**, Write a buffer overflow exploit that jumps to the winner function.  What is the flag that is printed?
5. For **program 2**, what menu option allows for the buffer overflow to occur?
6. For **program 2**, write a stack based buffer overflow POC & obtain a shell. Upload a writeup of your exploit that includes a discussion of:
    - How you identified the vulnerable code.
    - How you demonstrated overwriting the return pointer.
    - The method you used for gaining execution of your shellcode & how you found it.
    - Demonstration & screenshots of the POC working from the CLI demonstrating that you have gained shell.
7. **program 2** - Bonus Question > What is the admin password exactly?