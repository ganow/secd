# -*- coding: utf-8 -*-

from symbol import isSymbol

class Closure(object):
    def __init__(self, bv, body, env):
        super(Closure, self).__init__()
        if not isSymbol(bv):
            raise AttributeError('1st arg in Closure must be the Symbol class')
        self.bv = bv
        self.body = body
        self.env = env

    def __repr__(self):
        return '<clos %s, %s, %s>' % (self.bv, self.body, self.env)

def isClosure(symbol):
    return symbol.__class__ == Closure
