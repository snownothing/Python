# !/usr/bin/env python
# coding: utf-8

# print
def foo(s):
    n = int(s)
    print '>>> n = %d' % n
    return 10 / n
def main():
    foo('0')
# main()

# assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
# main()

#loggin
import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print 10 / n


# pdb

