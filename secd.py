# -*- coding: utf-8 -*-

import sys

from util_funcs import hd, tl, cons, assoc, derive, unitlist
from parse import Parser
from symbol import Symbol, isSymbol, isList, bind
from environment import Environment, find_var_in_env, find_list_in_env
from closure import Closure, isClosure
from lambda_eq import isLambdaEq, isCombination

class D0(object):
    def __init__(self):
        super(D0, self).__init__()
    def __repr__(self):
        return 'D0'
    def tostr(self):
        return self.__repr__()

def isD0(d):
    return d.__class__ == D0

class AP(object):
    def __init__(self):
        super(AP, self).__init__()
    def __repr__(self):
        return '`ap`'

def isAP(symbol):
    return symbol.__class__ == AP

class SECDMachine(object):
    def __init__(self, s=[], e=[], c=[], d=D0()):
        super(SECDMachine, self).__init__()
        self.s = s
        self.e = e
        self.c = c
        self.d = d

    def __repr__(self):
        return 'S: %s\nE: %s\nC: %s\nD: %s\n' % (self.s, self.e, self.c, self.d.tostr())

    def tostr(self):
        return '[<%s, %s, %s, %s>]' % (self.s, self.e, self.c, self.d)

    def update(self):

        if self.c == []:
            hd_d = hd(self.d)
            if isD0(hd_d):
                print 'reduction finished'
                return
            else:
                self.s = cons(hd(self.s), hd_d.s)
                self.e = hd_d.e
                self.c = hd_d.c
                self.d = hd_d.d
        else:

            hd_c = hd(self.c)

            if isSymbol(hd_c):
                self.s = [find_var_in_env(hd_c, self.e)]
                self.c = tl(self.c)
            elif isList(hd_c):
                self.s = [find_list_in_env(hd_c, self.e)]
                self.c = tl(self.c)
            elif isLambdaEq(hd_c):
                self.s = cons(Closure(hd_c.bv, hd_c.body, self.e), self.s)
                self.c = tl(self.c)
            elif isAP(hd_c):
                hd_s = hd(self.s)
                if isClosure(hd_s):

                    self.d = SECDMachine(tl(tl(self.s)),
                                         self.e,
                                         tl(self.c),
                                         self.d)

                    s_2nd = hd(tl(self.s))
                    self.s = []
                    self.e = derive(assoc(hd_s.bv, s_2nd), self.e)
                    self.c = unitlist(hd_s.body)
                else:
                    self.s = cons(hd_s(hd(tl(self.s))), tl(tl(self.s)))
            elif isCombination(hd_c):
                self.c = cons([hd_c.operand, hd_c.operator, AP()],
                               tl(self.c))

        print self
        self.update()

    def clear(self):
        self.s = []
        self.e = []
        self.c = []
        self.d = D0()

def dialog(secd, parser):
    buf = []
    i = 0
    print 'secd %d :> ' % i,

    for line in iter(sys.stdin.readline, ""):
        if line == '\n':
            if buf == []:
                print
                print 'secd %d :> ' % i,
                continue
            print

            code = parser.run(buf)
            secd.c = [code]
            secd.update()

            secd.clear()
            buf = []
            i += 1
            print
            print 'secd %d :> ' % i,
        else:
            buf.append(line)
            i += 1
            print
            print 'secd %d :> ' % i,


if __name__ == '__main__':

    secd = SECDMachine()
    parser = Parser()

    if len(sys.argv) == 2:
        print 'run script:', sys.argv[1]
        code = parser.run_from_file(sys.argv[1])
        secd.c = [code]
        print secd
        secd.update()

    else:
        print 'dialog mode'
        dialog(secd, parser)