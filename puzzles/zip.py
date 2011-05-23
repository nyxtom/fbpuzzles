#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import zipfile
colors = dict(red="\033[1;31m", nc="\033[0m")

def zip_puzzle(filename):
    zf = zipfile.ZipFile(filename + '.zip', mode='w')
    try:
        print 'Adding %s' % filename
        zf.write(filename)
    finally:
        zf.close()

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print '%sYou must provide an input filename%s' % (colors['red'], colors['nc'])
    else:
        zip_puzzle(sys.argv[1])
