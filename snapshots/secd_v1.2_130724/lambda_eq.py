# -*- coding: utf-8 -*-

from symbol import Symbol, isSymbol

class LambdaEq(object):
    def __init__(self, bv, body):
        super(LambdaEq, self).__init__()
        if bv.__class__ != Symbol:
            raise AttributeError('1st arg in LambdaEq must be the Symbol class')
        self.bv = bv
        self.body = body

    ## for debug
    # def __repr__(self):
    #     return 'LambdaEq(bv: %s, body: %s)' % (self.bv, self.body)

    def __repr__(self):
        return '(lambda %s: %s)' % (self.bv, self.body)

class Combination(object):
    def __init__(self, operator, operand):
        super(Combination, self).__init__()
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return '(%s %s)' % (self.operator, self.operand)

def isLambdaSymbol(symbol):
    if not isSymbol(symbol):
        return False
    else:
        return symbol.isEqual(Symbol('lambda'))

def isLambdaEq(eq):
    return eq.__class__ == LambdaEq

def isCombination(eq):
    return eq.__class__ == Combination