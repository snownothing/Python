# !/usr/bin/env python
# coding: utf-8

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 00:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

bart = Student('Bart Simpson', 98)

print bart._Student__name
