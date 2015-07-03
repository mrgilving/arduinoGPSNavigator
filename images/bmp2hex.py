#!/usr/bin/env python

import sys

f = list(open(sys.argv[1]).read())
flen = len(f)
width = int(sys.argv[2])
height = int(sys.argv[3])

res = []
for y in range(height):
    line = []
    for x in range(width):
        b1 = f.pop()
        b2 = f.pop()
        b3 = f.pop()
        if b3 == '\xff':
            line.append('0')
        else:
            line.append('1')
    #line.reverse()
    res.append(line)
print 'static const unsigned char PROGMEM %s[] = {' % sys.argv[1].replace('.bmp', '')
res.reverse()
while res:
    line = res.pop()
    bline = []
    while line:
        byte = []
        for i in range(8):
            byte.append(line.pop() if line else '0')
        byte = '0b%s%s' % (''.join(byte), ',' if res or line else '')
        print byte,
    print
print '};'

