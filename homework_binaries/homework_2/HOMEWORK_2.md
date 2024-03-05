### Context
Given binaries for this homework:
`./hw2p1` and `./hw2p2`

### Questions
#### Question 1
Manual Format String Write Calculations

In a hypothetical program, you are exploiting a format string vulnerability.  You will need to write the value 0xdeadbeef into the address 0xffeeffee.  Fill in the blanks for your payload that completes this overwrite:
```
\xee\xff\xee\xff + \xf0\xff\xee\xff + %[    ]x + %[    ]$hn + %[    ]x + %[    ]$hn
```

---

#### Question 2
Program 1 (Question 1):
In this series of questions, you will be working with the binary "hw2p1".
**For this question, ASLR should be off on your VM and in GDB.**
Your assignment: write a proof of concept exploit script using pwntools & python3 that successfully gets a shell using the "ret2popret" approach.  Upload your proof of concept script here.  Your proof-of-concept script should run simply by executing your script in the same directory with the binary hw2p1 - pwntools should start the binary as part of the script.

Required: "binPath=./hw2p1".  Do not set an absolute binpath (e.g. /home/kail/HW2/...).  You will lose points if you do not set a relative path with this exact file name.

Discussion: The ret2popret approach takes advantage of having a pointer to your buffer passed as an argument to your function.  That is what is happening here... but just one "pop ret" gadget isn't going to do it.  You'll need to string together a series of gadgets that "ret" to your payload.  Additionally, there are bad characters that you'll need to look out for.  This means you'll need to encode your payload appropriately.  Your payload should spawn an interactive shell on the local box (do not provide a bind shell or reverse shell payload).

If you cannot exploit the vulnerability, upload a detailed walkthrough of your analysis with discussion & screenshots showing your progress. If you successfully exploit the binary, you need only upload your POC.

---

Program 1 (Question 2):
What are all of the bad characters in program 1?  Remember, bad characters are ones that will either terminate your payload, or will not make it into your final payload.  You will need a careful eye to spot all of them.

Write your list of bad characters below and submit.  Provide your bad characters in numerical order from lowest to highest.  Any submission that are not in order will get 0 points.  E.g. if your bad characters are 0x02, 0x01, 0xfb, you should list them as, "0x01, 0x02, 0xfb".

Your Answer:

---

Program 1 (Question 3):
For program 1, if you pause program execution at the "ret" instruction of the vulnerable function (e.g. the function you are buffer-overflowing), what is the offset from the top of the stack to the pointer to your buffer?  Provide your answer in decimal format.

Remember GDB provides offsets in hexadecimal, you will need to convert from hex to decimal if using the "stack" command in GDB.  So if the offset from ESP to the pointer to your buffer (the thing you will be looking to use to pop-ret) is at offset 0x4c in GDB, the correct answer would be "76".  This is just an example of how to present your answer.

---

#### Question 3
In this series of questions, you will be working with the binary "hw2p2".  

For this question, ASLR should be ON on your VM (but need not be on in GDB while you are practicing).

Your assignment: write a proof of concept exploit script using pwntools & python3 that successfully gets a shell by exploiting a format string vulnerability in the program.  In particular:

Leak the addresses of the GOT & the winner function.
Use these to overwrite an address in the GOT with the address of the "winner" function (which will spawn you a shell).  
Your proof-of-concept script should run simply by executing your script in the same directory with the binary hw2p2 - pwntools should start the binary as part of the script. Required: "binPath=./hw2p2".  Do not set an absolute binpath (e.g. /home/kail/HW2/...).  You will lose points if you do not set a relative path with this exact file name.

---
