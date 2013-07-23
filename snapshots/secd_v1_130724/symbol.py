# -*- coding: utf-8 -*-

class Symbol(object):
    def __init__(self, name, content=None):
        super(Symbol, self).__init__()
        self.name = name
        self.content = content

    ### for debug
    # def __repr__(self):
    #     return 'Symbol(%s)' % self.name

    def __repr__(self):
        return self.name

    def isEqual(self, rhs):
        if self.__class__ != rhs.__class__:
            return False
        elif self.name == rhs.name:
            return True
        else:
            return False

def isSymbol(symbol):
    if symbol.__class__ == Symbol:
        return True
    else:
        return False

def isList(symbol):
    return symbol.__class__ == list

def bind(symbol, content):
    if symbol.__class__ != Symbol:
        raise AttributeError('bind() is only use for Symbol.')

    return Symbol(symbol.name, content)

