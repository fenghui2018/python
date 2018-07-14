#!/usr/bin/python
# -*- coding: utf-8 -*-

fp = open('text.txt', 'r+')

print type(fp)

for line in fp.readlines():
    print type(line), line.replace('\n', '')

print fp.tell()
print 'write--------------------'
fp.write('haha\n')
#fp.flush()

fp.seek(0)
print 'read--------------------'
for line in fp.readlines():
    print type(line), line.replace('\n', '')

fp.close()
