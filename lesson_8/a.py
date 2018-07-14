#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from b import xxx
import b

import mypackage.b

print xxx

s, t = 1, 2

print b.add(s, t)
print mypackage.b.sub(s, t)

print sys.path
