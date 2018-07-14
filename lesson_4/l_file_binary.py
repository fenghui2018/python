#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct

fp = open('xiaoyu.png', 'rb')

fp.seek(8)
print struct.unpack('>i', fp.read(4))[0]
fp.seek(16)
print 'width: ', struct.unpack('>i', fp.read(4))[0]
print 'height: ', struct.unpack('>i', fp.read(4))[0]

fp.close()
